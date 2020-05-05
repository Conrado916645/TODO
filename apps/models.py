from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class TodoModel(db.Model):
    id = db.Column('id', db.Integer,primary_key=True)
    title = db.Column('title', db.String(100),nullable=False)
    remarks = db.Column('remarks',db.Text(),nullable=False)
    date_create = db.Column('date_created',db.DateTime,default=datetime.today())

    def __init__(self, title, remarks):
        self.title = title
        self.remarks = remarks

    @classmethod
    def all(cls):
        return cls.query.all()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = _id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete_to_db(self):
        db.session.delete(self)
        db.session.commit()
        return True

    def __repr__(self):
        return 'Todo ({id}, {title}, {remarks})'.format(
            id = self.id,
            title = self.title,
            remarks = self.remarks
        )
