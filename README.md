# process-luncher-django
## How to use
when the server is activate for exemple at localhost:1234
on the maon directory we send a POST with the next JSON:
```JSON
{
    "cmd": "PING 192.168.1.80",
    "dir": "C:\\...\\RELESE\\Hand Reader.exe",
    "cwd": "C:\\...\\RELESE"
}
```

the  response will be contain the request and the exitcode + stdout of the command
```JSON
{
    "request": {
        "cmd": "PING 192.168.1.80",
        "dir": "C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE\\Hand Reader.exe",
        "cwd": "C:\\Users\\Shlomo\\source\\repos\\Hand Reader\\OUTPUT\\RELESE"
    },
    "response": {
        "exit Code": 3,
        "stdout": "Enterd with PING\r\nPING\r\nUnable to reach Authentication manger\r\nPort of socket 3001\r\nConnection established\r\nConnection Disposed\r\nUnable to reach Authentication manger\r\n"
    }
}
```
