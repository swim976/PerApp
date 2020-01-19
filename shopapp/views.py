from django.shortcuts import render
from django.http import HttpResponse
from .models import AddressInfo
# Create your views here.

from django.views.decorators.csrf import csrf_exempt


def save_address(res):
    return ''


@csrf_exempt
def address_test(res):
    """地址保存接口"""
    if res.method == 'POST':
        respost = res.POST
        addr = AddressInfo(
            name=respost.get('name', 'zdy'),
            address=respost.get('address', 'zdy'),
            phone=respost.get('phone', 'zdy'),
            receiving=0,
        )
        addr.save()
    return HttpResponse('address test')
