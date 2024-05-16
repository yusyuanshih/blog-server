from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.sql import func

from app.extensions.db import db


class Log(db.Model):
    id = Column(
        Integer,
        primary_key=True,
    )
    user_id = Column(
        Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    action = Column(
        String(32),
        nullable=False,
    )
    timestamp = Column(
        DateTime(timezone=True),
        default=func.now(),
        index=True,
    )
