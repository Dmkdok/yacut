import random
import string

from yacut.models import URLMap


def get_unique_short_id(length=6):
    """Генерирует уникальный короткий идентификатор заданной длины."""

    characters = string.ascii_letters + string.digits
    while True:
        short_id = ''.join(random.choice(characters) for _ in range(length))
        if not URLMap.query.filter_by(short=short_id).first():
            return short_id
