from django.db import models

KEYTYPE_CHOICES = (
    ('RSA', 'ssh-rsa'),
    ('DSA', 'ssh-dsa'),
    ('ECC-256', 'ecdsa-sha2-nistp256'),
    ('ECC-384', 'ecdsa-sha2-nistp384'),
    ('ECC-521', 'ecdsa-sha2-nistp521'),
)

class Node(models.Model):
    name = models.CharField(unique=True, primary_key=True, max_length=256)
    hostname = models.CharField(blank=True, max_length=256)
    public_keys = models.ManyToManyField('OpensshKey')

    def __unicode__(self):
        return self.name

class OpensshKey(models.Model):
    name = models.CharField(unique=True, max_length=256)
    keytype = models.CharField(max_length=6, choices=KEYTYPE_CHOICES)
    key = models.TextField()
    host = models.CharField(max_length=256, blank=True)

    def __unicode__(self):
        return self.name
