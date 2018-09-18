

<b> Prototype code</b>


Entire code [proto.py](https://github.com/LorenvXn/mu3/blob/master/Jupyter_approach/python3_code/prototype/proto.py) depends on the value provided for "service" key.
<i> Also, do provide all the values you need (master IP, minion IP, containerimage...etc)</i>

Make sure you provide the right path for configuration file conf.json.

Just run "python proto.py" ... and that's it!

As per conf.json:

```
{ "master": "127.0.0.1",
 "minion2":"127.0.0.1",
 "containerimage" : "kafka",
 "tagimage" : "v3",
 "service" : "kafka",
 "namecontainer" : "mumu",
 "porthost" : "9092",
 "portcontainer" : "9092",
 "amountgb" : "1G"}
 ```
 
below output will be obtained:


```
root@remote_host:/opt/remote_shift/kafka# docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                    NAMES
672ab82e672e6        2e6264348888        "/bin/bash"         8 seconds ago       Up 2 seconds        0.0.0.0:9092->9092/tcp   mumu
```

```
root@remote_host:/opt/remote_shift/kafka# docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
kafka               v3                  2e6264348888        28 seconds ago      1.01 GB
ubuntu              16.04               1a1a5a1a1e1a        12 days ago         115 MB
```
