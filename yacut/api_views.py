import re

from flask import jsonify, request

from settings import CUSTOM_ID_LENGTH, CUSTOM_ID_PATTERN
from yacut import app, db
from yacut.error_handlers import InvalidAPIUsage
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_short_link():

    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')

    url = data.get('url')
    custom_id = data.get('custom_id')

    if not url:
        raise InvalidAPIUsage('"url" является обязательным полем!')

    if custom_id:

        if len(custom_id) > CUSTOM_ID_LENGTH or not re.match(
            CUSTOM_ID_PATTERN, custom_id
        ):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )

        if custom_id and URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )

    else:
        custom_id = get_unique_short_id()

    new_url = URLMap(original=url, short=custom_id)
    db.session.add(new_url)
    db.session.commit()

    return jsonify(new_url.to_dict()), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        return jsonify({'message': 'Указанный id не найден'}), 404

    return jsonify({'url': url_map.original})
