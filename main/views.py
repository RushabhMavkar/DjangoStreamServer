from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from django.http.response import JsonResponse, FileResponse

import urllib.parse
import os

from . import forms
from . import models
from . import os_functions
from . import helper_functions


def logout_page(request):
    logout(request)
    return redirect('main_login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main_dashboard')

    form = forms.LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("main_dashboard")
    data = {'form': form}
    return render(request, 'main/login.html', data)


def signup_page(request):
    form = forms.Signup(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            user = User.objects.create_user(username=username, password=password, first_name=name)
            user.save()
    data = {'form': form}
    return render(request, 'main/signup.html', data)


@login_required
def dashboard(request):
    server_info = models.UserAccess.objects.filter(user=request.user).first()
    data = {'server_info': server_info}
    return render(request, 'main/dashboard.html', data)


@login_required
def create_server(request):
    form = forms.CreateServer(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = request.user
            name = form.cleaned_data.get('name')
            is_secure = form.cleaned_data.get('is_secure')
            access = form.cleaned_data.get('access')
            # TODO -- check is path is valid or not
            server = models.Server.objects.create(admin=user, name=name, is_secure=is_secure, access=access)
            models.UserAccess.objects.create(user=user, server=server, is_admin=True, activated=True)
            return redirect('main_dashboard')
    data = {'form': form}
    return render(request, 'main/create-server.html', data)


@login_required
def view_server_files(request):
    p = request.POST.get('path')
    server_info = models.UserAccess.objects.get(user=request.user)
    path = urllib.parse.unquote_plus(p) if p else server_info.server.access
    files = os_functions.get_files(path)
    data = {'files': files}
    return render(request, 'main/file-viewer.html', data)


@login_required
@api_view(['POST'])
def api_view_server_files(request):
    p = request.POST.get('path')
    path = urllib.parse.unquote_plus(p) if p else models.UserAccess.objects.get(user=request.user).server.access
    if os.path.isfile(path):
        request.session['file_path'] = path
        return JsonResponse('Success', safe=False)
    files = os_functions.get_files(path)
    data = {'files': files}
    return JsonResponse(data)


@login_required
def serve_file(request):
    path = request.session.get('file_path')
    return FileResponse(open(path, 'rb'))


@login_required
def share_qrcode(request):
    ip = helper_functions.get_ip()
    port = 8000
    helper_functions.create_qrcode(port)
    data = {'ip': ip, 'port': port}
    return render(request, 'main/share-qrcode.html', data)


@login_required
def join_server(request):
    form = forms.JoinServer(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            code = form.cleaned_data.get('server_code')
            server = models.Server.objects.filter(code=code)
            if server.exists():
                models.UserAccess.objects.create(user=request.user, server=server.first())
                return redirect('main_dashboard')
            else:
                print('Invalid')
    data = {'form': form}
    return render(request, 'main/join-server.html', data)


@login_required
def delete_server(request):
    server = models.UserAccess.objects.get(user=request.user, is_admin=True).server
    server.delete()
    return redirect('main_dashboard')


@login_required
def view_video(request):
    file_path = request.session.get('file_path')
    file_name = file_path.split("\\")[-1]
    data = {'file_name': file_name}
    return render(request, 'main/video-player.html', data)


@login_required
def users_connected(request):
    server = models.UserAccess.objects.get(user=request.user, is_admin=True).server
    users_joined = models.UserAccess.objects.filter(server=server).order_by('-is_admin')
    data = {'users': users_joined}
    return render(request, 'main/users-connected.html', data)
