from django.db import models
#关联用户表
from django.contrib.auth.models import User
# Create your models here.
#标签表:与文章表存在多对多
#title:标签标题
class Tag(models.Model):
    title=models.CharField(max_length=20,)
    def __str__(self):
        return self.title


#分类表:与文章表存在一对多
#title:分类标题
class Category(models.Model):
    title = models.CharField(max_length=20,)

    def __str__(self):
        return self.title






#文章表:与标签表多对多
class Article(models.Model):
    title = models.CharField(max_length=30, )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    create_time=models.DateTimeField(auto_now=True)
    update_time=models.DateTimeField(auto_now_add=True)
    author =models.ForeignKey(User,on_delete=models.CASCADE)
    views=models.IntegerField(default=0)
    Body=models.TextField(default=0)
    tags=models.ManyToManyField(Tag,)

    def __str__(self):
        return self.title








