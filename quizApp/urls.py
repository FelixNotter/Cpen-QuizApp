from django.urls import path
from . import views

urlpatterns = [
    path('suggestion',views.suggestion,name='suggestion'),
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('quiz/<str:catgry>/',views.quiz_view,name='quiz-view'),
    path('progress',views.progress,name='progress'),
    path('leader',views.leader,name='leader'),
]
