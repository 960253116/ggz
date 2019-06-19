from django.conf.urls import url
#引入视图函数模块
from.import views
app_name="blog"
urlpatterns=[
    #首页路由
    url(r'^$',views.IndexView.as_view(),name="index")


]