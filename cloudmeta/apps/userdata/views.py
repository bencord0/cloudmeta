from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from cloudmeta.apps.userdata.models import Node
from cloudmeta.apps.metadata.views import _get_node

def index(request):
    return HttpResponse("user-data service: {meta[REMOTE_ADDR]}".format(meta=request.META))

def user_data(request):
    node = _get_node(request)
    userdata = node.userdata
    return HttpResponse(userdata.data)
    
