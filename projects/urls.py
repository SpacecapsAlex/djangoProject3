from django.urls import path
from projects import views

urlpatterns = [
    path('', views.create_project, name='index'),
]