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
    path('server/join/', views.join_server, name='main_join_server'),
    path('server/delete/', views.delete_server, name='main_delete_server'),
    path('server/users/', views.users_connected, name='main_users_connected'),

    path('view/file/', views.serve_file, name='main_serve_file'),
    path('view/video/', views.view_video, name='main_video_player'),

    path('qrcode/', views.share_qrcode, name='main_share_qrcode'),
]
