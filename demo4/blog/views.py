from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import *
#首页
class IndexView(View):
    def get(self,req):
        #获取所有的文章
        articles=Article.objects.all()
        #获取所有的技能
        skills = Skill.objects.all()
        return render(req,"blog/index.html",locals())

# class skillView(View):
#     def get (self,req,):
#         skills=skill.objects.all()
#         return render(req,"blog/index.html",loc
#         als())

class CharacterView(View):
    def get(self,req):
        introduce=Introduce.objects.all()
        rolelists=Rolelist.objects.all()
        return render(req,"blog/character.html",locals())

class AboutView(View):
    def get(self,req):
        about=About.objects.all()
        print(about)
        return render(req,"blog/about.html",locals())

class BlogView(View):
    def get(self,req):
        blogs=Blogs.objects.all()
        archive=Archive.objects.all()
        return render(req, "blog/blog.html", locals())