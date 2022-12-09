from django.urls import path

from authapp.apps import AuthappConfig
from authapp import views

app_name = AuthappConfig.name

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('edit/', views.EditView.as_view(), name='edit'),
]
