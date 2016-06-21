
from mongoengine import *
from mongoengine.fields import SequenceField, DateTimeField
from djangoQuiz.settings import DBNAME

connect(DBNAME, host='mongodb://inquizzit:inquizzit@ds025752.mlab.com:25752/heroku_5tgn5grt')
# connect(DBNAME)


class Options(EmbeddedDocument):
    """docstring for Options."""

    option_one = StringField(max_length=600, required=True)
    option_two = StringField(max_length=600, required=True)
    option_three = StringField(max_length=600, required=True)
    option_four = StringField(max_length=600, required=True)
    option_five = StringField(max_length=600, required=True)


class Question(EmbeddedDocument):
    """docstring for Answers."""

    QID = SequenceField()
    question_text = StringField(max_length=600, required=True)
    # options = ReferenceField('Options', reverse_delete_rule=0)
    options = ListField(EmbeddedDocumentField(Options))
    answer = StringField(max_length=200, required=True)


class Quiz(Document):
    """docstring for Quiz."""

    name = StringField(max_length=200, required=True)
    question = ListField(EmbeddedDocumentField(Question))
    # question = ReferenceField('Question', reverse_delete_rule=0)
    # pass_mark = IntField(min_value=0, max_value=100)

class Detail(EmbeddedDocument):
    score = IntField(max_length=200, required=True)
    course_name = StringField(max_length=200, required=True)
    date = DateTimeField()


class UserDetails(Document):
    """docstring for Quiz."""

    username = StringField(max_length=200, required=True)
    user_detail = ListField(EmbeddedDocumentField(Detail))

