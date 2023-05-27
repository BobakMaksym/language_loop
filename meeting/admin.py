from django.contrib import admin
from .models import Language, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'language')
    search_fields = ('title', )
    list_filter = ('language', )


class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Language, LanguageAdmin)
admin.site.register(Post, PostAdmin)
