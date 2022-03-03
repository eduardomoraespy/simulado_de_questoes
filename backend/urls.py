
from django.contrib import admin
from django.urls import path

from quiz_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home),
    path('quiz', home.quiz)
]
