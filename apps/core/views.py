from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.applications.models import Application

@login_required
def home(request):
    applications = Application.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "core/home.html", {"applications": applications})