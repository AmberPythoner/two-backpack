from django.db import models

# Create your models here.

class Play(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lan = models.CharField(max_length=60)
    len = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name