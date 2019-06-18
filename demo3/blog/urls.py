from django.conf.urls import url
from.import views
from haystack.views import SearchView
app_name="blog"
urlpatterns=[
    # url(r'^$',views.IndexView.as_view(),name="index")
    url(r'^$', views.index, name="index"),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name="single"),
    url(r'^search/$',SearchView(),name="search")

]