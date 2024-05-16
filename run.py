import os
from app import app

if __name__ == "__main__":
    port = os.environ.get("PORT")
    host = os.environ.get("HOST")

    print(f"Listening {host}:{port}")

    app.run(
        host=host,
        port=port,
    )
