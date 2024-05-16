from flask_cors import CORS

from app.config import CORS_ORIGINS

cors = CORS(
    resources={"*": {"origins": CORS_ORIGINS}},
    supports_credentials=True,
)
