from django.db import models

class Node(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=256)
    userdata = models.ForeignKey('UserData')

    def __unicode__(self):
        return self.name

class UserData(models.Model):
    name = models.CharField(unique=True, max_length=256)
    data = models.TextField()

    def __unicode__(self):
        return self.name
