from django.db import models

# Create your models here.
# class Tag(models.Model):
#     title=models.CharField(max_length=20)
#文章表
class Article(models.Model):
    title=models.CharField(max_length=30)
    create_time= models.DateTimeField(auto_now=True)
    body=models.TextField()

    def __str__(self):
        return self.title
