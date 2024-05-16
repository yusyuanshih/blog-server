from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
)
from sqlalchemy.sql import func

from app.extensions.db import db


class PostLike(db.Model):
    id = Column(
        Integer,
        primary_key=True,
    )
    created_at = Column(
        DateTime(timezone=True),
        default=func.now(),
        index=True,
    )
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    post_id = Column(
        Integer,
        ForeignKey("post.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
