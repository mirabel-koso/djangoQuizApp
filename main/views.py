from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from main.models import Quiz, Options, Question
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.

def home_view(request):
    return render(request, 'main/index.html')


class AdminView(TemplateView):

    template_name = 'main/admin.html'

    def post(self, request, *args, **kwargs):
        quiz_name = request.POST.get('quiz_name', '')
        question_text = request.POST.get('question_text', '')
        option1 = request.POST.get('option1', '')
        option2 = request.POST.get('option2', '')
        option3 = request.POST.get('option3', '')
        option4 = request.POST.get('option4', '')
        option5 = request.POST.get('option5', '')
        question_answer = request.POST.get('question_answer', '')

        options = Options(
            option_one=option1,
            option_two=option2,
            option_three=option3,
            option_four=option4,
            option_five=option5,
        )

        options.save()

        question = Question(
            question_text=question_text,
            answer=question_answer,
            options=options)
        question.save()
        quiz = Quiz(
            name=quiz_name, question=question)
        quiz.save()

        return HttpResponseRedirect(reverse_lazy('adminquestion'))
