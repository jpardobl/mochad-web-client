# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Device
import re
import netcat


class X10CommandNotSupportedError(Exception):
    pass


def home(request):
    devices = Device.objects.all()
    return render_to_response("home.html", {"devices": devices, })


def cmd(request, cmd_line=None):
    if not re.match("^pl\s[apAP]\d{1,2}\s(on|off|On|Off)$", cmd_line):
        raise X10CommandNotSupportedError(cmd_line)
    ret = netcat.command(cmd_line)
    return HttpResponse("OK - %s" % ret)


def open_all(request):

    ret = netcat.command("pl A1 extended_code_1 0 5")
    return HttpResponse("OK - %s" % ret)

def close_all(request):
    ret = netcat.command("pl A1 extended_code_1 0 11")
    return HttpResponse("OK - %s" % ret)
