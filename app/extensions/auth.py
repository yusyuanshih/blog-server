from flask_login import LoginManager

# Local modules
from app.models import User
from app.utils import GoogleAPIClient

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(id: int):
    return User.query.get(id)


googleAPI = GoogleAPIClient(
    'identitytoolkit',
    'v2',
    ['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/identitytoolkit'],
    )