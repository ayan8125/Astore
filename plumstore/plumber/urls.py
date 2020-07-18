from django.urls import path
from . import views
from orders.views import order1
from hire.views import user_hire,hire_plumber,hires1,hire_electricians,hire_repairer,plumber_hire,electricians_hire
from plumber.views import editProfile,not_auth



urlpatterns = [
    path('', views.home, name='plum-home'),
    path('about/', views.about, name='plum-about'),
    path('<str:usernames>/profile/', views.profile, name='profile'),
    path('<str:usernames>/editProfile/', editProfile, name='editProfile'),
    path('/NotAUTHENTICATED/', not_auth, name='not_auth'),
    path('<str:usernames>/orders/',order1, name='orders'),
    path('<str:usernames>/hires/',hires1, name='hires'),
    path('<str:usernames>/', views.valid_user, name='valid_user'),
    path('<str:usernames>/hire1/', user_hire, name='user_hire'),
    path('<str:usernames>/plumber_hire/', plumber_hire, name='plumber_hire'),
    path('<str:usernames>/electricians_hire/', electricians_hire, name='electricians_hire'),
    path('<str:usernames>/hire-plumber/', hire_plumber, name='hire-plumber'),
    path('<str:usernames>/hire-electricians/', hire_electricians, name='hire-electricians'),
    path('<str:usernames>/hire-repairer/', hire_repairer, name='hire-repairer'),
    #    path('logout/', views.logouts, name='logout'),
     
]
