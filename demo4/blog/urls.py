from django.conf.urls import url
#引入视图函数模块
from.import views
app_name="blog"
urlpatterns=[
    #首页路由
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^character/$',views.CharacterView.as_view(),name="character"),
    url(r'^about/$',views.AboutView.as_view(),name="about"),
    url(r'^blog/$',views.BlogView.as_view(),name="blog"),

]