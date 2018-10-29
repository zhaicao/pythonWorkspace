from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from sign.models import Event, Guest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
            # 返回重定向
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            # 返回HttpResponse对象
            return render(request, 'index.html', {'error': 'username or password error!'})

# 发布会管理
# 通过使用login_required装饰器限制视图必须登录
@login_required
def event_manage(request):
    # 读取浏览器的cookie
    #username = request.COOKIES.get('user', '')
    username = request.session.get('user', '')
    # 获取Event全部数据
    event_list = Event.objects.all()
    return render(request, "event_manage.html", {'user': username, "events": event_list})

@login_required
def search_name(request):
    username = request.session.get('user', '')
    search_name = request.GET.get('name', '')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request, "event_manage.html", {"user": username,
                                                 "events": event_list})
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list, 2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page不是整数取第一页数据
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果page不在范围，取最后一页
        contacts = paginator.page(paginator.num_pages)
    return render(request, "guest_manage.html", {"user": username,
                                                 "guests": contacts})
