from django.db import models

# Create your models here.
class Blog_post(models.Model):
    """ Create new blog post """
    title = models.CharField(max_length=60)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    
    def __str__(self):
        """ Return string representation of the title"""
        return self.title