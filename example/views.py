from django.http import HttpResponse
from .models import User, Post, Comment


# Create your views here.


def index(request):
    # пагинация - разбиение на страницы
    number_of_elements = 10
    users = User.objects.all()[: number_of_elements]  # пропустить 1 элемент с начала и взять 3 элемента
    return HttpResponse(users)


def create(request):
    user = User(
        name='Tom',
        email='tom@gmail.com',
        password='123',
        phone='123456789',
        birthday='1990-01-01',
        description='test'
    )
    user.save()
    return HttpResponse('create')


def edit(request):
    # number_of_user = User.objects.filter(name='Tome').update(password='password', age=20)  # обнавление только одного поля(name) - выполниться 1 запрос
    user = User.objects.get(id=1)
    user.name = 'Bob'
    user.save(update_fields=['name'])  # обнавление только одного поля(name)
    # user.save()  - обнавление всех полей
    return HttpResponse('edit')


def delete(request):
    user = User.objects.filter(name='Tom').exists()
    if user:
        User.objects.filter(name='Tom')
    return HttpResponse('delete')


def get_user_from_post(request):
    user = Post.objects.filter(user_id=12)  # получить все посты пользователя с id=12
    # user_name = Comment.objects.get(id=1).user.name - получить имя пользователя, который оставил комментарий с id=1
    # user_name = Post.objects.get(id=1).user.name - получить имя пользователя, который оставил пост с id=1
    return HttpResponse(user)
