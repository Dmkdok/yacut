from datetime import datetime, timezone

from flask import url_for

from settings import CUSTOM_ID_LENGTH, ORIGINAL_LINK_LENGTH
from yacut import db


class URLMap(db.Model):
    """
    Модель для хранения информации о коротких и оригинальных ссылках.
    """

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(ORIGINAL_LINK_LENGTH), nullable=False)
    short = db.Column(db.String(CUSTOM_ID_LENGTH), unique=True, nullable=False)
    timestamp = db.Column(
        db.DateTime, index=True, default=datetime.now(timezone.utc)
    )

    def to_dict(self):
        """Возвращает данные в виде словаря."""

        return dict(
            url=self.original,
            short_link=url_for(
                'redirect_short_url', short=self.short, _external=True
            ),
        )
