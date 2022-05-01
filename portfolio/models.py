from django.db import models

class Project(models.Model):
    title = models.CharField(max_length = 100, default = '')
    description = models.TextField(max_length = 300, default = '')
    image = models.ImageField(upload_to = 'portfolio/image/')
    url = models.URLField(blank = True)

    def __str__(self):
        return self.title
