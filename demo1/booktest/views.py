
from django.http import HttpResponse
#引入可操作html
from django.template import loader
from .models import BookInfo,HeroInfo
# Create your views here.
def index(req):
     # return HttpResponse("这里是首页")
    #获取模板
    temp = loader.get_template("booktest/index.html")
     #2.获取数据
    res =temp.render({"username":"ggz","age":20})
    return HttpResponse(res)

def list(req):
    # return HttpResponse("这里是列表页")
    #获取模板
    #获得所有的书
    books=BookInfo.objects.all()
    print(books)
    temp=loader.get_template("booktest/list.html")
    res =temp.render({"books":books})
    return HttpResponse(res)

# def detail(req,id):
#     # book=BookInfo.objects.get
#     return HttpResponse("这里是%s" % (id,))

def detail(req, id):
    book =BookInfo.objects.get(pk=id)
    temp = loader.get_template('booktest/detail.html')
    res = temp.render({"book":book})

    return HttpResponse(res)