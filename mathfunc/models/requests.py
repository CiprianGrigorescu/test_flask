from sqlalchemy import func

from mathfunc.app_main import db


class Requests(db.Model):
    __tablename__ = 'requests'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    request_verb = db.Column(db.String(10), nullable=False)
    request_method = db.Column(db.String(30), nullable=False)
    request_params = db.Column(db.String(255), nullable=False)
    added = db.Column(db.DateTime, default=func.now())
