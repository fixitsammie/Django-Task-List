from django.db import models

# Create your models here.


class Task(models.Model):
    item = models.CharField(max_length=2000)
    updated = models.DateTimeField(blank=True,null=True)
    created = models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.item