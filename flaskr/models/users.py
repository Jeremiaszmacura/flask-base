from flaskr.config import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    surname = db.Column(db.String(80))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}