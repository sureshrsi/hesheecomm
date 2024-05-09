from django.urls import path
from adminapp import views
urlpatterns = [
    path('signup', views.signup)
]
