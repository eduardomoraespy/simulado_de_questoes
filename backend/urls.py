
from django.contrib import admin
from django.urls import path, include


from quiz_app.views import home
from backend.rotas import instituicoes


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('quiz/', home.quiz, name='quiz'),
    
    path("", include(instituicoes)),
]
