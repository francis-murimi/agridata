from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()

    class Meta:
        def __str__(self):
            return self.title


class Upload(models.Model):
    title = models.CharField(max_length= 30, default= 'News')
    textfile = models.FileField(upload_to='documents')
    status = models.BooleanField(default=False)
    class Meta:
        def __str__(self):
            return self.title
