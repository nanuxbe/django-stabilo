from django.contrib import admin
from stabilo.models import Category, Keyword

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

class KeywordAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
admin.site.register(Keyword, KeywordAdmin)
