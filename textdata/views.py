from django.template import loader
from .models import Blog, Upload
from django.http import HttpResponse, Http404,HttpResponseRedirect
import json

def home(request):
    blogs = Blog.objects.all()
    total = blogs.count()
    
    uploads = Upload.objects.all()
    utotal = uploads.count()
    
    read_uploads = Upload.objects.filter(status= True)
    read_total = read_uploads.count()
    
    
    return HttpResponse(json.dumps({'total':total, 'uploaded_total':utotal, 'read_total':read_total}), content_type="application/json")

def read_file(request):
    files = Upload.objects.filter(status = False)
    for file in files:
        a = file.title
        b = file.textfile.path
        f = open(b, 'r')
        contents =f.read()
        new_blog = Blog(title= a, text= contents)
        new_blog.save()
        file.status = True
        file.save()
    return HttpResponse(contents)

