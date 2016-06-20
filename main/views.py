
# from django.shortcuts import render
from django.views.generic.base import TemplateView
from main.models import Quiz, Options, Question, UserDetails, Detail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
# from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['quizzes'] = Quiz.objects.all()
        return self.render_to_response(context)


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

        question = Question(
            question_text=question_text,
            answer=question_answer,
            options=[options])
        quizname = Quiz.objects(name=quiz_name)
        if quizname:
            quizname.update(push__question=question)

        else:
            quiz = Quiz(
                name=quiz_name, question=[question])
            quiz.save()

        return HttpResponseRedirect(reverse_lazy('adminquestion'))


class ViewUsers(TemplateView):

    template_name = 'main/all_users.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['user_detail'] = UserDetails.objects.all()
        return self.render_to_response(context)


class TakeQuizView(TemplateView):
    template_name = 'main/quiz.html'

    def get(self, request, *args, **kwargs):
        quiz_name = self.kwargs.get('quizname')
        context = self.get_context_data(**kwargs)
        context['quiz_questions'] = Quiz.objects(name=quiz_name)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        quiz_name = self.kwargs.get('quizname')
        question = {}
        answer = {}
        name = request.POST
        for key, value in name.iteritems():
            if key.isdigit():
                answer[key] = value[-1]
            if key.startswith('group'):
                question[key[-1]] = value[-1]
        for key in answer:
            val = []
            if key.isdigit():
                val.append(int(key))

        min_val = min(val)
        count = 0
        for i in xrange(len(question)):
            num = i + min_val
            if question.get(str(num)) == answer.get(str(num)):
                count = count + 1
        score = (count / float(len(question)) * 100)

        details = Detail(
            score=score,
            course_name=quiz_name
        )

        user_already_exist = UserDetails.objects(username=request.user.username)
        if user_already_exist:
            user_already_exist.update(push__user_detail=details)
        else:
            user_details = UserDetails(
                username=request.user.username,
                user_detail=[details]
            )

            user_details.save()

        return HttpResponseRedirect(reverse_lazy('user_profile'))


class UserProfile(TemplateView):
    template_name = 'main/user_profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['one_user_detail'] = UserDetails.objects(username=request.user.username)
        return self.render_to_response(context)
