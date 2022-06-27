from django.contrib import admin
from .models import Blog, Upload
#from import_export import resources
from import_export.admin import ImportExportModelAdmin


"""
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title',]
    list_filter = ['title',]
    #list_editable = ['title',]
    #exclude = ('text',)

class UploadAdmin(admin.ModelAdmin):
    list_display = ['title','status']

admin.site.register(Blog, BlogAdmin)
admin.site.register(Upload, UploadAdmin)
"""



@admin.register(Blog)
class BookAdmin(ImportExportModelAdmin):
    pass

@admin.register(Upload)
class AuthorAdmin(ImportExportModelAdmin):
    pass
