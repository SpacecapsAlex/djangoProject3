from django.http import HttpResponse
from django.shortcuts import render

from example.models import User
from .models import Project
from .forms import ProjectForm

# Create your views here.


def create_project(request):
    user_list = User.objects.all()
    project = ProjectForm()
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        users = request.POST.getlist('users')
        projects = Project.objects.filter()
        if project_form.is_valid():
            project = Project(
                name=project_form.cleaned_data['name'],
                description=project_form.cleaned_data['description'],
                lead_name=project_form.cleaned_data['lead_name'],
                count_users=len(users),
            )

            project.save()

            project.users.set(users)

            # for user in users:
            #     project.users.add(user)

            # some_list = request.POST.getlist('ex')
            # print(some_list)
            return HttpResponse(project.count_users)

    data = {
        'form': project,
        'users': user_list,
    }
    return render(request, 'projects/create_project.html', context=data)


def get_projects(request):
    projects = Project.objects.all()
    data = {
        'projects': projects,
    }
    return render(request, 'projects/get_projects.html', context=data)
