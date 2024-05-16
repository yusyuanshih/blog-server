from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    LargeBinary,
)
from sqlalchemy.sql import func

from app.extensions.db import db


class Comment(db.Model):
    id = Column(
        Integer,
        primary_key=True,
    )
    text = Column(
        LargeBinary,
        nullable=False,
    )
    text_hash = Column(
        LargeBinary,
        nullable=False,
    )
    text_iv = Column(
        LargeBinary,
        nullable=False,
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
