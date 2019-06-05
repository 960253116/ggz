from django.contrib import admin
from.models import BookInfo,HeroInfo
# Register your models here.



class HeroInfoInlines(admin.StackedInline):
    model=HeroInfo
    extra=1
#显示时间
class BookInfoAdmin(admin.ModelAdmin):
    #重写list_display 重写后台显示哪些字段
    list_display = ("title","pub_date")
    list_filter = ("title","pub_date")
    list_per_page = 20
    inlines=[HeroInfoInlines]
#在注册模型的时候,注册改模型的后台管理类 通过管理类重写后


#
class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ("name","content")
    list_filter=("name")
    search_fields = ("name","content")
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)
