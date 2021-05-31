from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    path('new/', views.NewContact.as_view()),
    path('update/', views.UpdateContact.as_view())
]
