from django.contrib import admin
from .models import Social

# Register your models here.
@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display= ('email', 'adress', 'phone')
    search_fields= ('email',)
    list_filter= ('phone', )
    row_id_fields=['email']