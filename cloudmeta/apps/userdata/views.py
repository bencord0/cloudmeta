from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from cloudmeta.apps.userdata.models import Node

def _get_node(request):
    remote_addr = request.META['REMOTE_ADDR']
    try:
        node = Node.objects.get(name=remote_addr)
    except Node.DoesNotExist:
        # Possible ipv4->ipv6 conversion?
        node = get_object_or_404(Node, name=remote_addr.lstrip('::ffff:'))
    return node

def index(request):
    return HttpResponse("user-data service: {meta[REMOTE_ADDR]}".format(meta=request.META))

def user_data(request):
    node = _get_node(request)
    userdata = node.userdata
    return HttpResponse(userdata.data)
    
