from django.contrib import admin
from cloudmeta.apps.metadata.models import Node, OpensshKey

admin.site.register(Node)
admin.site.register(OpensshKey)
