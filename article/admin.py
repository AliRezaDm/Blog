from django.contrib import admin
from .models import Article, Category



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent','status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug':('title',)}
    
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag','slug', 'jpublish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'discription')
    prepopulated_fields = {'slug':('title',)}
    ordering =  ['status', 'publish']
    actions = ["make_published", "make_drafted"]

admin.site.register(Article, ArticleAdmin)

# Register your models here.
