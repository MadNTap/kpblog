from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)