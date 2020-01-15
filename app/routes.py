from app import application, api, db
from .models import Question, Vote
from flask_restplus import Resource, reqparse
from collections import Counter

from flask import jsonify


vote_parser = reqparse.RequestParser()
vote_parser.add_argument('winner_id', type=int, required=True, help='id of winning contender')
vote_parser.add_argument('loser_id', type=int, required=True, help='id of losing contender')


@api.route('/hello')
class HelloWorld(Resource):
    
    #@api.doc(parser=None)
    def get(self):
        '''Hello World'''
        return jsonify('Hello world')


@api.route('/<question_name>/contenders')
class QuestionContenders(Resource):

    def get(self, question_name):
        '''Get some contenders for a given question'''
        question = Question.query.filter_by(name=question_name).first()
        contenders = [(i.name, i.id) for i in question.contenders]
        return jsonify(contenders)


@api.route('/<question_name>/vote')
class VoteApi(Resource):

    @api.doc(parser=vote_parser)
    def post(self, question_name):
        '''Vote for a given question'''
        args = vote_parser.parse_args()
        question = Question.query.filter_by(name=question_name).first()
        contender_ids = [i.id for i in question.contenders]
        if args['winner_id'] in contender_ids and args['loser_id'] in contender_ids:
            vote = Vote(winner_id=args['winner_id'], loser_id=args['loser_id'], question_id=question.id)
            db.session.add(vote)
            db.session.commit()
        return None

@api.route('/<question_name>/results')
class Results(Resource):

    def get(self, question_name):
        '''Get some contenders for a given question'''
        question = Question.query.filter_by(name=question_name).first()
        contenders = {int(i.id): i.name for i in question.contenders}
        votes = [(i.winner_id, i.loser_id) for i in question.votes]
        wins = Counter([i[0] for i in votes])
        losses = Counter([i[1] for i in votes])
        totals = {contender: wins.get(contender, 0) + losses.get(contender, 0) for contender in contenders.keys()}
        ratios = [(contenders[id_], wins.get(id_, 0)/totals[id_]) for id_ in contenders.keys() if totals[id_] >= 5]
        return jsonify(sorted(ratios, key=lambda x: x[1], reverse=True))