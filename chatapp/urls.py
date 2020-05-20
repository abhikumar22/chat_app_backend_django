"""chatapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url

from userchatapp.api import Login, GetAllUsers, AddChat, GetAllChat,AddBlog,GetAllBlog
# ,getData

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^login$', Login.as_view()),
    url('^getAllUsers$', GetAllUsers.as_view()),
    url('^getAllChat$', GetAllChat.as_view()),
    url('^addChat$', AddChat.as_view()),
    url('^addBlog$', AddBlog.as_view()),
    url('^getAllBlogs$', GetAllBlog.as_view()),
]
