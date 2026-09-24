from django.urls import path
from .views import *
urlpatterns = [
    path('students/',StudentData.as_view(),name='StudentData'),
    path('studentDetail/<int:id>',StudentDetail.as_view(),name='StudentDetail'),
    path('quiz/',QuizAPI.as_view(),name='Quiz'),
    path('question/',QuestionAPI.as_view(),name='Question'),
    path('option/',OptionAPI.as_view(),name='Option'),
    path('participant/',ParticipantAPI.as_view(),name='Participant'),
    path('quizResult/',QuizResultAPI.as_view(),name='QuizResult'),
]