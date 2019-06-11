from django.db import models

# Create your models here.
"""
数据模型模块 MVT中的M
"""
class topicInfo(models.Model):
    title=models.CharField(max_length=20)
    def __str__(self):
        return self.title


class NameInfo(models.Model):
    name = models.CharField(max_length=20)
    vote=models.IntegerField(default=0)
    topic=models.ForeignKey(topicInfo,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



