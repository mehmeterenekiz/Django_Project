from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'author', 'slug')
    search_fields= ('title', 'content', 'author')
    list_filter= ('author', )
    row_id_fields=['author']