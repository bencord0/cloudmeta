from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from cloudmeta.apps.latest.models import Node


def _get_node(request):
    remote_addr = request.META['HTTP_X_REAL_IP'] or request.META['REMOTE_ADDR']
    try:
        node = Node.objects.get(name=remote_addr)
    except Node.DoesNotExist:
        # Possible ipv4->ipv6 conversion?
        node = get_object_or_404(Node, name=remote_addr.lstrip('::ffff:'))
    return node


def index(request):
    return HttpResponse("cloudmeta service: {}".format(
        request.META['HTTP_X_REAL_IP'] or request.META['REMOTE_ADDR']))


def hostname(request):
    node = _get_node(request)
    return HttpResponse(node.hostname)


def sshkey(request, idx=0):
    '''
    The default and defacto usage of key indexes is to use the zero'th key.
    I don't know who uses the other indexes, and what for.

    So I'm going to use the 0th index to mean all keys configured, then you
    can pick out individual keys using the ith-1 index.
    '''
    node = _get_node(request)
    sshkeys = node.sshkeys.all()
    if int(idx) > 0:
        sshkeys = [sshkeys[int(idx) - 1]]

    response = '\n'.join([sshkey.data for sshkey in sshkeys])
    return HttpResponse(response)
    

def userdata(request):
    node = _get_node(request)
    userdata = node.userdata
    return HttpResponse(userdata.data)
