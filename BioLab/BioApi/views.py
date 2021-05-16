from django.shortcuts import render,HttpResponse,Http404
from django.views.generic import View
from django.http import HttpRequest,JsonResponse
import subprocess
from subprocess import STDOUT
from django.views.decorators.csrf import csrf_exempt



import json

# Create your views here.

@csrf_exempt
def main_call(req:HttpRequest,*args,**kwargs):
    if req.method == 'GET':
        return HttpResponse('This here for fun\nWe only implemented post with json format<br> such as \n{\n"cmd":"PING 192.168.1.80",\n"dir":"C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE\\Hand Reader.exe",\n"cwd":"C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE"\n}',200)
    elif req.method == 'POST':
        j = json.loads(req.body)
        parms = j.get('args',None)
        cwd = j.get('cwd',None)
        args =[j.get('exe',None)]
        timeout = j.get('timeout',5)
        if parms is None or cwd is None or args is None:
            return JsonResponse({"status":404,"msg":"One or more parms is empty"})
        for p in parms.split(" "):
            args.append(p)
        t = {}
        stdout = ""
        try:
            p = subprocess.run(args,cwd=cwd,capture_output=True,timeout=timeout)
            t['response'] = {
            'exit Code': p.returncode,
            'stdout': p.stdout.decode('utf-8'),
            'stderr':p.stderr.decode('utf-8')
            }
            t['status'] = 200
        except subprocess.TimeoutExpired as e:
            t['Excpetion'] = "The progam timeout"
            t['response'] = {
            'exit Code': "No exit",
            'stdout':e.stdout.decode('utf-8'),
            'stderr':e.stderr.decode('utf-8')
            }
            t['status'] = 408
        finally:
            t['request'] = j
            
        
        
        return JsonResponse(t)
