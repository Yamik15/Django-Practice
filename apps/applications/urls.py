from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_app, name='create_app'),
    path('add_review/<int:app_id>/', views.add_review, name='add_review')
]
