from django.db import models

class Posts(models.Model):
    Category_Choice = (
        ('N-Agr', 'News'),
        ('Agr', 'Agriculture')
    )
    url = models.URLField(blank= True)
    text = models.TextField(blank=True)
    prediction = models.BooleanField(blank= True, null=True)
    category = models.CharField(max_length=300, choices = Category_Choice,blank= True)
    
    def __str__(self):
        return self.url