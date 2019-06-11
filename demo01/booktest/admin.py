from django.contrib import admin
from .models import NameInfo,topicInfo
# Register your models here.
admin.site.register(topicInfo)
admin.site.register(NameInfo)