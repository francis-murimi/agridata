from django.contrib import admin
from .models import Posts

#class BlogAdmin(admin.ModelAdmin):
    #list_display = ['url',]
    #list_filter = ['title',]
    #list_editable = ['title',]
    #exclude = ('text',)
# Register your models here.
admin.site.register(Posts)