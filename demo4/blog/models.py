from django.db import models

# Create your models here.
# class Tag(models.Model):
#     title=models.CharField(max_length=20)
#文章表
class Article(models.Model):
    title=models.CharField(max_length=30)
    create_time= models.DateTimeField()
    body=models.TextField()
    pic = models.ImageField(upload_to='picture')

    def __str__(self):
        return self.title
#技能表
class Skill(models.Model):
    name=models.CharField(max_length=30)
    pic = models.ImageField(upload_to="picture")
    def __str__(self):
        return self.name

# class Picture(models.Model):
#     pic = models.ImageField(upload_to='picture')
#     kill = models.OneToOneField(skill, on_delete=models.CASCADE)
# #图片表 与技能表有多对一的关系
# class picture(models.Model):
#     pic=models.ImageField(upload_to="picture")
#     desc=models.CharField(max_length=20)
#     url=models.CharField(max_length=20)
#     def __str__(self):
#         return self.desc

#人物介绍
class Introduce(models.Model):
    pic = models.ImageField(upload_to="picture")
    title = models.CharField(max_length=30)
    body = models.TextField()
    pics = models.ImageField(upload_to="picture")
    def __str__(self):
        return self.title
#角色列表
class Rolelist(models.Model):
    name=models.CharField(max_length=30)
    # pic = models.ImageField(upload_to="picture")
    def __str__(self):
        return self.name

class About(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    def __str__(self):
        return self.title

class Blogs(models.Model):
    title = models.CharField(max_length=30)
    create_time = models.DateTimeField()
    body = models.TextField()
    pic = models.ImageField(upload_to='picture')
    def __str__(self):
        return self.title


class Archive(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name