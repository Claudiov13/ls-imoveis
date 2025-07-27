# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 1) Login
    path('login/', auth_views.LoginView.as_view(
        template_name='core/login.html'
    ), name='login'),

    # 2) Logout (POST) → volta à página de login
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # 3) Todas as rotas do seu app "core"
    path('', include('core.urls', namespace='core')),
]
