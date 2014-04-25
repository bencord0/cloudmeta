from django.contrib import admin
from cloudmeta.apps.latest.models import Node, SshKey, UserData

admin.site.register(Node)
admin.site.register(SshKey)
admin.site.register(UserData)
