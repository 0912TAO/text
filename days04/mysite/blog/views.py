from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse

# Create your views here.
from . import models

def successfully(request):
    '''
    成功的视图函数，--显示成功登陆信息提示
    :param request:
    :return:
    '''
    return render(request, "blog/successfully.html", {})
def failed(request):
    '''
    失败界面显示--信息显示
    :param request:请求对象
    :return:
    '''
    return render(request, "blog/failde.html", {})
def add_article(request):
    '''
    添加用户--测试版
    :param request:
    :return:
    '''
    return render(request, "blog/add_article.html", {})
    # return render(request,"blog/add_article",{})
def delete_article(request):
    '''
    删除的视图函数，完成都对用户的删除功能实现
    :param request: 请求对象
    :return:
    '''
    u_id = request.GET["id"]
    article = models.Article.objects.get(pk=u_id)
    article.delete()
    return render(request, "blog/successfully.html", {"msg1": "删除成功"})
def login(request):
    '''
    登录的视图函数，完成用户的登录功能
    :param request:请求对象
    :return:
    '''
    if request.method == "GET":
        return render(request,"blog/index.html",{"msg1":"请登陆"})
    elif request.method =="POST":
        #接受参数
        username=request.POST["loginname"]
        password=request.POST["loginpassword"]
        try:
            article=models.Article.objects.get(username=username,password=password)
            request.session["loginArticle"]=article
            return render(request,"blog/successfully.html",{"msg1": "登陆成功"})
        except:
            return render(request, "blog/failed.html", {"msg1": "登录失败，请重新登录！！"})
def logout(req):
    try:
        del req.session["loginArticle"]
    finally:
        return redirect(reverse("blog:index"))
def update(request,u_id):
    '''
    更新的视图函数，完成用户的信息更新与完善
    :param request: 请求参数
    :param u_id: 参数
    :return:
    '''
    if request.method == "GET":
        article = models.Article.objects.filter(id=u_id).first()
        return render(request, "blog/update.html", {"article": article})
    else:
        nickname = request.POST["nickname"]
        age = request.POST['age']
        email = request.POST['email']
        article = models.Article.objects.get(pk=u_id)
        article.age = age
        article.nickname = nickname
        article.email=email
        article.save()
        return redirect("/blog/show/" + str(u_id) + "/")
        # return redirect(reverse("/blog/show.html"))
def show(request,u_id):
    '''
    展示的视图函数，展示用户信息
    :param request:
    :param u_id:
    :return:
    '''
    article = models.Article.objects.get(pk=u_id)
    return render(request, "blog/show.html", {"article": article})
def list_article(request):
    '''
    所有用户展示的视图函数
    :param request:
    :return:
    '''
    articles = models.Article.objects.all()
    return render(request, "blog/list_article.html", {'articles':articles})
def index(request):
    '''
    主界面的视图函数
    :param request:
    :return:
    '''
    if request.method =='GET' :
        return render(request,"blog/index.html",{"msg":"请认真填写信息"})
    elif request.method == "POST":
        # 接受参数
        try:
            username = request.POST["username"].strip()
            password = request.POST.get("password").strip()  # .getlist()
            querpassword = request.POST.get("querpassword").strip()
            nickname = request.POST.get("nickname", None)

            # 数据校验
            if len(username) < 1:
                return render(request, "blog/failed.html", {"msg1": "用户名称不能为空！！"})
            if len(password) < 6:
                return render(request, "blog/failed.html", {"msg1": "密码长度不能小于6位！！"})
            if password != querpassword:
                return render(request, "blog/failed.html", {"msg1": "两次密码不一致！！"})
            # 用户名称是否重复

            models.Article.objects.filter(username=username)

            # 保存数据
            article = models.Article(username=username, password=password, nickname=nickname)
            article.save()
            return render(request, "blog/successfully.html", {"msg1": "恭喜您，注册成功！！"})

        except:
            return render(request, "blog/failed.html", {"msg1": "对不起，用户名称不能为空！！"})
