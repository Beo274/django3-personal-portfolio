from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100, default = '')
    data = models.DateField()
    description = models.TextField(default = '')
    image = models.ImageField(upload_to = 'portfolio/image/', blank = True)

    def __str__(self):
        return self.title
