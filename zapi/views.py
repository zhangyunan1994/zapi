import logging

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from zapi.forms import LoginForm

logger = logging.getLogger(__name__)


def index(request):
    return render(request, "index.html")


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                logger.info("+" * 100)
                logger.info(f"({username}) 登陆了")
                logger.info("+" * 100)
                return HttpResponseRedirect('/')
            else:
                logger.error("x" * 100)
                logger.error(f"({username}) 尝试登录，输入了错误的密码({password})")
                logger.error("x" * 100)
                return render(request, 'login.html', {'form': form, 'error_msg': "用户名或密码错误"})
        else:
            return render(request, 'login.html', {'form': form})


@login_required
def logout(request):
    logger.info("-" * 100)
    logger.info(f"({request.user.username}) 登出了")
    logger.info("-" * 100)
    auth.logout(request)
    return HttpResponseRedirect("login")
