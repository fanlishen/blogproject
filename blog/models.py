from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField('类名', max_length=20)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签',max_length=100)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published')
    )
    title = models.CharField('标题', max_length=70)
    body = models.TextField('正文')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now_add=True)
    status=models.CharField('文章状态', max_length=1,choices=STATUS_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    excerpt = models.CharField('摘要', max_length=54, blank=True, null=True, help_text="可选，如若为空将摘取前54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category', verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk':self.pk})

