from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from sign.models import Event, Guest

# Create your views here.
def index(request):
    return render(request, "index.html")

# 登录
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('pwd', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # 设置cookie
            # response.set_cookie('user', username, 3600)
            request.session['user'] = username
            auth.login(request, user)
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

# 发布会管理
# 通过使用login_required装饰器限制视图必须登录
@login_required
def event_manage(request):
    # 读取浏览器的cookie
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    event_list = Event.objects.all()
    return render(request, "event_manage.html", {'user': username, "events": event_list})
