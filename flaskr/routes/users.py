from flask import request, jsonify, Response, Blueprint

from flaskr.config import db
from flaskr.models.users import User


users_blueprint = Blueprint("users_blueprint", __name__)


@users_blueprint.route("/")
def hello_world() -> str:
    return "<p>Hello, World!</p>"


@users_blueprint.route("/users", methods=["GET", "POST"])
def users() -> Response:
    if request.method == "GET":
        users = User.query.all()
        data = [user.as_dict() for user in users]
        return jsonify(data)

    if request.method == "POST":
        name = request.json["name"]
        surname = request.json["surname"]
        new_user = User(name=name, surname=surname)
        db.session.add(new_user)
        db.session.commit()
        return f"<p>User with name: {name} and surname {surname} successfully added</p>"