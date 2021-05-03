from django.shortcuts import render,HttpResponse
from django.views.generic import View
from django.http import HttpRequest,JsonResponse
import subprocess
from django.views.decorators.csrf import csrf_exempt

import json

# Create your views here.

@csrf_exempt
def main_call(req:HttpRequest,*args,**kwargs):
    if req.method == 'GET':
        return HttpResponse('This here for fun\nWe only implemented post with json format<br> such as \n{\n"cmd":"PING 192.168.1.80",\n"dir":"C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE\\Hand Reader.exe",\n"cwd":"C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE"\n}',200)
    elif req.method == 'POST':
        j = json.loads(req.body)
        parms = j.get('cmd',None)
        cwd = j.get('cwd',None)
        cmd =[j.get('dir',None)]
        print(cwd)
        for p in parms.split(" "):
            cmd.append(p)
        p = subprocess.run(cmd,cwd=cwd,capture_output=True)
        t = {}
        t['request'] = j
        t['response'] = {
            'exit Code': p.returncode,
            'stdout':p.stdout.decode('utf-8')
        }
        
        
        return JsonResponse(t)
