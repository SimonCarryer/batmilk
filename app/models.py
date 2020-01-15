from app import db
from datetime import datetime

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    question_text = db.Column(db.String(500))
    contenders = db.relationship('Contender', backref='question', lazy='dynamic')
    votes = db.relationship('Vote', backref='question', lazy='dynamic')

    def __repr__(self):
        return '<Question {}>'.format(self.question_text)

class Contender(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), index=True)
    name = db.Column(db.String(500))

    def __repr__(self):
        return '<Contender {}>'.format(self.name)

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), index=True)
    winner_id = db.Column(db.Integer)
    loser_id = db.Column(db.Integer)