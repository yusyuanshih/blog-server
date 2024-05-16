import logging

from flask import Blueprint, jsonify
from flask_login import (
    login_user,
    login_required,
    logout_user,
    current_user,
)
from flask_mail import Message
from werkzeug.security import generate_password_hash, check_password_hash
from webargs import fields
from webargs.flaskparser import use_kwargs

from app.config import Config
from app.extensions.db import db
from app.extensions.mail import mail
from app.models import User, Log

auth_blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@auth_blueprint.route("/signup", methods=["POST"])
@use_kwargs(
    {
        "email": fields.Str(required=True),
        "name": fields.Str(required=True),
        "password": fields.Str(required=True),
    }
)
def signup(email: str, name: str, password: str):
    if User.query.filter_by(email=email).first():
        return ("電子信箱已被註冊", 400)

    if User.query.filter_by(name=name).first():
        return ("使用者名稱已被註冊", 400)

    user = User(
        email=email,
        name=name,
        password=generate_password_hash(password),
    )
    db.session.add(user)
    db.session.commit()
    login_user(user, remember=True)

    # 新增資料庫記錄
    log = Log(
        user_id=user.id,
        action="Signup",
    )
    db.session.add(log)
    db.session.commit()

    logging.info(f"User {user.name} registered.")

    # 發送註冊通知郵件
    if Config.MAIL_ENABLE:
        msg = Message("Registration Successful", recipients=[email])
        msg.body = "Thank you for registering!"
        mail.send(msg)

    return "註冊成功"


@auth_blueprint.route("/login", methods=["POST"])
@use_kwargs(
    {
        "email": fields.Str(required=True),
        "password": fields.Str(required=True),
    }
)
def login(email: str, password: str):
    user: User | None = User.query.filter_by(email=email).one_or_none()

    if user is None:
        logging.warning(f"Login failed for user {email}.")
        return ("電子信箱錯誤", 400)

    if not check_password_hash(user.password, password):
        logging.warning(f"Login failed for user {email}.")
        return ("密碼錯誤", 400)

    login_user(user, remember=True)

    # 新增登入記錄
    log = Log(
        user_id=user.id,
        action="Login",
    )
    db.session.add(log)
    db.session.commit()

    logging.info(f"User {user.name} logged in.")

    # 發送登入通知郵件
    if Config.MAIL_ENABLE:
        msg = Message("Login Notification", recipients=[email])
        msg.body = "You have logged in successfully."
        mail.send(msg)

    return jsonify(
        {
            "id": user.id,
            "name": user.name,
        }
    )


@auth_blueprint.route("/logout", methods=["POST"])
@login_required
def logout():
    # 新增登出記錄
    log = Log(
        user_id=current_user.id,
        action="Logout",
    )
    db.session.add(log)
    db.session.commit()

    logging.info(f"User {current_user.name} logged out.")

    logout_user()

    return "登出成功"


@auth_blueprint.route("/verify", methods=["GET"])
@login_required
def verify():
    return jsonify(
        {
            "id": current_user.id,
            "name": current_user.name,
        }
    )
