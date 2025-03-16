from django.db import models

# Create your models here.

class Social(models.Model):
    email = models.EmailField(max_length=254)
    adress = models.TextField()
    phone = models.CharField(max_length=20)
    github = models.CharField(max_length=50)
    linkedin = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50,default='https://www.instagram.com/mehmete_ekiz/')

    def __str__(self):
        return self.email

    class Meta: 
        ordering = ['email']
        verbose_name = 'Social'
        verbose_name_plural = 'Socials'