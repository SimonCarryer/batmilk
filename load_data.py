from app import db
from app.models import *

dont work though

data = {
        'text': 'Which milk would you rather drink?',
        'name': 'milk',
        'contenders': [
            'cow',
            'rabbit',
            'bat',
            'weasel',
            'aardvark',
            'rat',
            'hare',
            'guinea pig',
            'pig',
            'camel',
            'horse',
            'otter',
            'seal',
            'whale',
            'kangaroo',
            'tiger',
            'lion',
            'mouse',
            'sheep',
            'goat',
            'cat',
            'dog',
            'wolf',
            'llama',
            'panda',
            'bear',
            'anteater',
            'pangolin'
        ]
}

question = Question(name=data['name'], question_text=data['text'])
db.session.add(question)
db.session.commit()

question = Question.query.filter_by(name=data['name']).first()

for mammal_name in data['contenders']:
    mammal = Contender(question_id=question.id,
                        name=mammal_name)
    db.session.add(mammal)
db.session.commit()
