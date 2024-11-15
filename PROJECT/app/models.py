from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'User'


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('User', related_name='posts', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Post'
    