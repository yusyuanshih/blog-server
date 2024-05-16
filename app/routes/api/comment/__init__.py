import logging

from flask import Blueprint
from flask_login import (
    login_required,
    current_user,
)
from webargs import fields
from webargs.flaskparser import use_kwargs

from app.extensions.db import db
from app.models import Post, Comment, Log
from app.utils.hash import get_hash
from app.utils.cipher import encrypt, decrypt


comment_blueprint = Blueprint("comment", __name__, url_prefix="/comment")


@comment_blueprint.route("", methods=["POST"])
@use_kwargs(
    {
        "post_id": fields.Int(required=True),
        "text": fields.Str(required=True),
    }
)
@login_required
def create_comment(post_id: int, text: str):
    post: Post | None = Post.query.get(post_id)
    if post is None:
        logging.error("Failed to add a comment.")
        return "找不到貼文", 404

    text_iv, encrypted_text = encrypt(text)
    text_hash = get_hash(encrypted_text)
    comment = Comment(
        user_id=current_user.id,
        post_id=post_id,
        text=encrypted_text,
        text_hash=text_hash,
        text_iv=text_iv,
    )
    db.session.add(comment)
    db.session.commit()

    # 新增建立留言記錄
    log = Log(
        user_id=current_user.id,
        action="Comment",
    )
    db.session.add(log)
    db.session.commit()

    logging.debug(f"User {current_user} added a new comment.")

    return "新增成功"


@comment_blueprint.route("/<int:id>", methods=["DELETE"])
@login_required
def delete_comment(id: int):
    comment: Post | None = Comment.query.get(id)
    if comment is None:
        logging.error("Failed to delete a comment.")
        return "找不到留言"

    if current_user.id != comment.user_id:
        logging.error("Failed to delete a comment.")
        return "你沒有權限刪除"

    db.session.delete(comment)
    db.session.commit()

    # 新增刪除留言記錄
    log = Log(
        user_id=current_user.id,
        action="Delete-Comment",
    )
    db.session.add(log)
    db.session.commit()

    logging.debug(f"User {current_user} deleted a comment.")

    return "刪除成功"
