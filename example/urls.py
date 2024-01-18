from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('edit', views.edit),
    path('delete', views.delete),
    path('get-user-from-post', views.get_user_from_post),
]
