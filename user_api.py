import flask
from flask import jsonify

from data import db_session
from data.users import User

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    session = db_session.create_session()
    users = session.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('name', 'phone_number', 'address'))
                 for item in users]
        }
    )
