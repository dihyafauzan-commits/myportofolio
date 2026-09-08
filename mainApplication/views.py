from django.shortcuts import render

from .models import Experience


def show_main(request):
    context = {
        "name": "Dihya",
        "npm": "2506637003",
        "study_program": "S1 Ilmu Komputer KKI",
        "bio": (
            "A Computer Science student at Universitas Indonesia interested "
            "in software development and education."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Dihya",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)