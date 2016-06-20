# from django.db import models
# # from djangotoolbox.fields import EmbeddedModelField
# from django.core.validators import MaxValueValidator


# class Category(models.Model):
#     """docstring for Category."""

#     name = models.CharField(max_length=300)
#     description = models.TextField()
#     is_active = models.BooleanField(default=True)


# class Answers(object):
#     """docstring for Answers."""

#     answer_text = models.CharField(max_length=300)
#     is_correct = models.BooleanField()
#     display_order = models.IntegerField()


# class Question(object):
#     """docstring for Answers."""

#     question_type = models.CharField(max_length=1000)
#     question_text = models.CharField(max_length=1000)
#     # category = EmbeddedModelField('Category')
#     # answer = EmbeddedModelField('Answers')


# class Quiz(models.Model):
#     """docstring for Quiz."""

#     Name = models.CharField(
#         max_length=60, blank=False)

#     description = models.TextField(
#         blank=True, help_text='a description of the quiz')

#     # questions = EmbeddedModelField('Question')

#     pass_mark = models.SmallIntegerField(
#         blank=True, default=50,
#         help_text="Percentage required to pass exam.",
#         validators=[MaxValueValidator(100)])

#     success_text = models.TextField(
#         blank=True, help_text="Displayed if user passes.",
#         verbose_name="Success Text")

#     fail_text = models.TextField(
#         verbose_name="Fail Text",
#         blank=True, help_text="Displayed if user fails.")

#     def __str__(self):
#         return self.name

#     def questions_text(self):
#         return ", ".join([question.text for question in self.questions.all()])

from mongoengine import *
from mongoengine.fields import SequenceField
from djangoQuiz.settings import DBNAME

connect(DBNAME)


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


class UserDetails(Document):
    """docstring for Quiz."""

    username = StringField(max_length=200, required=True)
    user_detail = ListField(EmbeddedDocumentField(Detail))

