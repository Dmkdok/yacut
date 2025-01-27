from flask import redirect, render_template, url_for

from yacut import app, db
from yacut.forms import URLForm
from yacut.models import URLMap
from yacut.utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        custom_id = form.custom_id.data

        if custom_id and URLMap.query.filter_by(short=custom_id).first():
            return render_template(
                'index.html',
                form=form,
                error_message=(
                    'Предложенный вариант короткой ссылки уже существует.'
                ),
            )

        if not custom_id:
            custom_id = get_unique_short_id()

        new_url = URLMap(original=original_link, short=custom_id)
        db.session.add(new_url)
        db.session.commit()

        return render_template(
            'index.html',
            form=form,
            short_link=url_for(
                'redirect_short_url', short=custom_id, _external=True
            ),
        )

    return render_template('index.html', form=form)


@app.route('/<short>')
def redirect_short_url(short):
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
