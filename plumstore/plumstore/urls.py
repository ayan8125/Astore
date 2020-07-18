"""plumstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as users_view
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static
from hire.views import hire_plumber
from employes.views import mastersignup


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup1/', users_view.signup1, name='signup1'),
    path('signup2/', users_view.signup2, name='signup2'),
    path('signup3/', users_view.signup3, name='signup3'),
    path('login/', users_view.log, name='login'),
    path('logout/', users_view.logout, name='logout'),
    path('otp/', users_view.auth, name='auth'),
    path('base/', users_view.base, name='base'),
    path('test/', users_view.test, name='test'),
    path('email_confirm/<token>/',users_view.email_confirm, name='email_confirm'),
    path('mastersign/', mastersignup, name='mastersign'),
    path('', include('plumber.urls')),
 

  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)