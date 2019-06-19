from django.shortcuts import render
from django.views.generic import View
# Create your views here.
from .models import *
#首页
class IndexView(View):
    def get(self,req):
        articles=Article.objects.all()
        return render(req,"blog/index.html",locals())


