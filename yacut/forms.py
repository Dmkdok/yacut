from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from settings import CUSTOM_ID_LENGTH, CUSTOM_ID_PATTERN, ORIGINAL_LINK_LENGTH


class URLForm(FlaskForm):
    """Форма для создания короткой ссылки."""

    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(
                1,
                ORIGINAL_LINK_LENGTH,
                message=f'Максимум {ORIGINAL_LINK_LENGTH} символов',
            ),
            URL(message='Добавьте ссылку'),
        ],
    )
    custom_id = StringField(
        'Ваша кароткая ссылка',
        validators=[
            Length(
                1,
                CUSTOM_ID_LENGTH,
                message=f'Максимум {CUSTOM_ID_LENGTH} символов',
            ),
            Regexp(
                CUSTOM_ID_PATTERN,
                message='Только английские буквы, цифры и подчеркивание',
            ),
            Optional(),
        ],
    )
    submit = SubmitField('Создать')
