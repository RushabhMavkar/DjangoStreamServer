from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_page, name='main_login'),
    path('logout/', views.logout_page, name='main_logout'),
    path('signup/', views.signup_page, name='main_signup'),
    path('', views.dashboard, name='main_dashboard'),

    path('files/server/', views.view_server_files, name='main_view_files'),

    path('api/files/', views.api_view_server_files, name='main_api_view_files'),

    path('server/create/', views.create_server, name='main_create_server'),
    path('view/file/', views.serve_file, name='main_serve_file'),
]
