from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from cloudmeta.apps.metadata.models import KEYTYPE_CHOICES, Node

def _get_node(request):
    remote_addr = request.META['HTTP_X_REAL_IP'] or request.META['REMOTE_ADDR']
    try:
        node = Node.objects.get(name=remote_addr)
    except Node.DoesNotExist:
        # Possible ipv4->ipv6 conversion?
        node = get_object_or_404(Node, name=remote_addr.lstrip('::ffff:'))
    return node

def index(request):
    return HttpResponse("meta-data service: {}".format(
        request.META['HTTP_X_REAL_IP'] or request.META['REMOTE_ADDR']))

def hostname(request):
    node = _get_node(request)
    return HttpResponse(node.hostname)

def openssh_key(request, idx=0):
    node = _get_node(request)
    openssh_key = node.public_keys.all()[int(idx)]
    ssh_template = "{keytype} {key} {host}"

    return HttpResponse(ssh_template.format(
        keytype = dict(KEYTYPE_CHOICES)[openssh_key.keytype],
        key = openssh_key.key,
        host = openssh_key.host))
    
