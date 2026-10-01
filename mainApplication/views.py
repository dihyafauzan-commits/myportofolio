from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
import datetime
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied

import json
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseNotAllowed
from django.views.decorators.http import require_POST

from .models import Experience, Project
from .forms import ProjectForm


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'No active login session / Cookie not found')
    context = {
        "name": "Dihya Fauzan Haryadi",
        "npm": "2506637003",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def show_experience(request):
    context = {
        "name": "Dihya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_project(request):
    form = ProjectForm(request.POST or None)

    if not request.user.is_superuser:
        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Anda tidak memiliki akses untuk menambah data.</p>")

    form = ProjectForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_projects")

    context = {
        "name": "Dihya Fauzan Haryadi",
        "form": form,
        "is_update": False,
    }
    return render(request, "projects_form.html", context)

def show_projects(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Dihya Fauzan Haryadi",
        "title_query": title_query,
        "form": ProjectForm(),
    }
    return render(request, "project.html", context)

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(project.id),
            "fields": {
                "id": project.id,
                "title": project.title,
                "description": project.description,
                "tech_stack": project.tech_stack,
                "project_url": project.project_url,
                "project_image_url": project.project_image_url,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })

    return JsonResponse(data, safe=False)
    
@login_required(login_url="/login/")
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)

    if not request.user.is_superuser:
        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Anda tidak memiliki akses untuk menghapus data.</p>")

    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_projects")

    return redirect("main:show_projects")

@login_required(login_url="/login/")
def update_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    form = ProjectForm(request.POST or None, instance=project)

    if not (request.user.is_superuser or is_editor(request.user)):
        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Anda tidak memiliki akses untuk mengubah data.</p>")

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Data proyek berhasil diperbarui!")
        return redirect("main:show_projects")

    context = {
        "name": "Dihya Fauzan Haryadi",
        "form": form,
        "project": project,
        "is_update": True,
    }

    return render(request, "projects_form.html", context)

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Account created successfully. Please log in.")
        return redirect("main:login")

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Burhan",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return redirect("main:show_main")

@login_required(login_url="/login/")
@require_POST
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    user = request.user

    if project.starred_by.filter(id=user.id).exists():
        project.starred_by.remove(user)
    else:
        project.starred_by.add(user)

    return redirect("main:show_projects")

def is_editor(user):
    return user.groups.filter(name='Editor').exists()

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'mainApplication/project.html', {'projects': projects})

@login_required
def project_create(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Anda tidak memiliki akses untuk membuat data.")
    
    # Logika form submission di sini
    return render(request, 'mainApplication/project_form.html')

@login_required
def project_update(request, pk):
    if not (request.user.is_superuser or (request.user)):
        return HttpResponseForbidden("Anda tidak memiliki akses untuk mengubah data.")
    
    project = get_object_or_404(Project, pk=pk)
    # Logika form update di sini
    return render(request, 'mainApplication/project_form.html', {'project': project})

@login_required
def project_delete(request, pk):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Anda tidak memiliki akses untuk menghapus data.")
    
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'mainApplication/project_confirm_delete.html', {'project': project})

def project_json_endpoint(request):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'], "Metode tidak diizinkan")
    projects = Project.objects.all()
    data = []
    
    for p in projects:
        data.append({
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'total_stars': p.total_stars(),
        })
        
    return JsonResponse(data, safe=False)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Only the portfolio owner can add projects."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Project added successfully.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

@login_required
@require_POST
def add_project_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"error": "Anda tidak memiliki hak akses untuk menambah proyek."}, 
            status=403
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        
        messages.success(request, "Project added successfully!")
        
        return JsonResponse({
            "message": "Proyek berhasil ditambahkan!",
            "project": {
                "id": project.id,
                "title": project.title
            }
        }, status=201)
    
    return JsonResponse({"errors": form.errors}, status=400)