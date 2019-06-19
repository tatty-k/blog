from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'blog_id': self.id})

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    created = models.DateTimeField(default=now)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('comment_delete', kwargs={
            'blog_id': self.blog.id,
            'pk': self.id
        })
