from django.conf.urls import url
from main import views


urlpatterns = [

    url(r'^admin/quiz/$',
        views.AdminView.as_view(),
        name='adminquestion'
        ),
]
