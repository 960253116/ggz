from django.shortcuts import render,get_object_or_404
from django.views.generic import View,ListView,DetailView
from .models import *
from comments.forms import CommentForm
from django.views.decorators.cache import cache_page

# Create your views here.

class IndexView(View):

    # @cache_page(60*5)
    def get(self,req):

        articles=Article.objects.all()
        # page=getpageinfo(req,atricles,2,"/")
        return render (req,"blog/index.html",locals())
@cache_page(60*5)
def index(req):
    articles = Article.objects.all()
    # page=getpageinfo(req,atricles,2,"/")
    return render(req, "blog/index.html", locals())

class SingleView(View):
    def get(self,req,id):
        article=get_object_or_404(Article, pk=id)
        #向详情页面传递一个评论表单
        # cf=CommentForm
        return render (req,"blog/single.html", locals())

    # def post(self,req,id):
    #     cf=