from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.CharField(max_length=255, null=True, blank=True)
    slug = models.SlugField(unique=True,blank=True)
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
            return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    class Meta: 
        ordering = ['-created_at'] #oluşturulma tarihine göre sıralansın ama eksi koyduk ki en son oluşturulan ilk görünsün.
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
