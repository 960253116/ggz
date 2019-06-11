# from django.shortcuts import render
# # from django.http import HttpResponse
# # """
# # MVT中的V 视图模块
# # """
# # # Create your views here.
# # def index(req):
# #     return HttpResponse("这里是首页")
# # #
# # def list(req):
# #     return HttpResponse("这里是投票页")

from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from .models import topicInfo,NameInfo
# Create your views here.
from django.views.generic import View
# class LoginView(View):
#     def get(self,req):
#         return render(req,"polls/login.html")
#
#     def post(self, req):
#         username = req.POST.get("username")
#         pwd = req.POST.get("password")
#         # cookie实在response里设置
#         res = redirect(reverse("polls:index"))
#         res.set_cookie("username", username)
#         return res

#用装饰器装饰一下
def checklogin(fun):
    def check(req,*args):
        # if req.COOKIES.get('username'):
        #     return func(req,*args)

        if req.session.get("username"):
            return fun(req,*args)

        else:
            return redirect(reverse('booktest:login'))
    return check



@checklogin
def index(req):
    # return HttpResponse("index")
    return render(req, 'booktest/index.html',{ "username":"ggz" })
@checklogin
def detail(req,id):
    # return HttpResponse("detail %s"% id)
    if req.method == "GET":
        top = topicInfo.objects.get(pk=id)
        return render(req, 'booktest/detail.html', locals())
    elif req.method == "POST":
        c_id=req.POST.get('ppt')
        res=NameInfo.objects.get(pk=c_id)
        res.vote+=1
        res.save()
        return redirect(reverse('booktest:result',args=(id,)))

        # res = NameInfo.objects.get(name=req.POST.get('ppt'))
        # res.option += 1
        # res.save()
        # top=topicInfo.objects.get(pk=id)
        # return render(req, 'booktest/result.html', locals())
        # return HttpResponse('qqq')
@checklogin
def list(req):
    vote1 = topicInfo.objects.all()
    return render(req, 'booktest/list.html', {"vote1": vote1})
    # return HttpResponse("list")
@checklogin
def result(req, id):
    top=topicInfo.objects.get(pk=id)
    return render(req, 'booktest/result.html', {'top':top})

def login(req):
    if req.method == "GET":
        return render(req,"booktest/login.html")
    elif req.method =="POST":
        username = req.POST.get("username")
        pwd=req.POST.get("password")
        req.session["username"]=username
        return redirect(reverse("booktest:index"))
        #cookie实在response里设置
        # res = redirect(reverse("booktest:index"))
        # res.set_cookie("username", username)
        # return res