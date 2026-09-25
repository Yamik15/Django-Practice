from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.applications.models import Application

@login_required
def create_app(request):
    if request.method == "POST":
        Application.objects.create(
            user=request.user,
            course=request.POST.get("course", ""),
            start_date=request.POST.get("start_date", ""),
            payment=request.POST.get("payment_method", "")
        )
        return redirect("home")
    return render(request, "applications/create.html")

@login_required
def add_review(request, app_id):
    application = get_object_or_404(Application, id=app_id, user=request.user)
    if application.status != "completed":
        return redirect("home")
    if request.method == "POST":
        application.review = request.POST.get("review", "")
        application.save()
        return redirect("home")
    return render(request, "applications/add_review.html", {"application": application})