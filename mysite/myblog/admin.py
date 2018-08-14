from django.contrib import admin
from myblog.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]

class CategoryAdmin(admin.ModelAdmin):
    # inlines = [
    #     CategoryInline,
    # ]
    exclude = ('members',)

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
