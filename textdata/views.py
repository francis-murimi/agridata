from django.template import loader
from .models import Blog, Upload
from django.http import HttpResponse, Http404,HttpResponseRedirect
import json

def home(request):
    template = loader.get_template('textdata/home.html')
    context = {}
    return HttpResponse(template.render(context,request))

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

