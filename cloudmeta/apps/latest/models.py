from django.db import models


class Node(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=256)
    hostname = models.CharField(blank=True, max_length=256)
    sshkeys = models.ManyToManyField('SshKey')
    userdata = models.ForeignKey('UserData')

    def __str__(self):
        return self.name
    __unicode__ = __str__


class SshKey(models.Model):
    name = models.CharField(unique=True, max_length=256)
    key = models.TextField()

    def __str__(self):
        return self.name
    __unicode__ = __str__


class UserData(models.Model):
    name = models.CharField(unique=True, max_length=256)
    data = models.TextField()

    def save(self, *args, **kwargs):
        def strip_crlf(text):
            return text.replace('\r\n', '\n')
        self.data = strip_crlf(self.data)
        super(UserData, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    __unicode__ = __str__
