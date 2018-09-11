<b> Ship a containerized architecture with the help of Ansible 2.6 </b>

<i> still working on it... </i>

For more details on flow, check the diagram: [Diagram Flow](https://github.com/LorenvXn/mu3/blob/master/flow.txt) 

<b> Folders ierarchy on master host </b>

What <b>/opt</b> folder contains:
```
root@master#tree -d /opt
/opt
|
├── local_blueprint
│   ├── kafka
│   └── zookeeper
│   .
│   .
│   .
│   └── the n-th service 
│
├── local_images
│   ├── kafka
│   └── zookeeper
│   .
│   .
│   .
│   └── the n-th image you need to deploy
|
├── local_shift
│   ├── kafka
│   └── zookeeper
│   .
│   .
│   .
│   └── n-th folder of the service you need to deploy
├── play
├── remote_shift           // only if you want to deploy services on master 
    ├── kafka
    └── zookeeper
    .
    .
    .
```

/opt/local_blueprint

```
root@master:/opt# tree /opt/local_blueprint/
/opt/local_blueprint/
|
├── blueprint_param_run_container.sh
├── kafka
│   └── blueprint_run_image.sh
└── zookeeper
    └── blueprint_run_image.sh


```

What <b> opt/local_shift </b> subfolder contains:

```
root@master# tree /opt/local_shift/
/opt/local_shift/
├── kafka
│   ├── param_run_container.sh
│   └── run_image.sh
├── zookeeper
│   ├── param_run_container.sh
│   └── run_image.sh
.
.
.
└── zookeeper
    ├── param_run_container.sh
    └── run_image.sh

```

What <b> /opt/play </b> subfolder contains:

```
root@master:/opt# tree /opt/play
/opt/play
├── main.yaml
├── kafka.yaml
└── zookeeper.yaml
.
.
.
└── the_nth_service.yaml

```

<b> Folders ierarchy on remote hosts </b>


What <b> /opt/remote_shift </b> subfolder contains
```
root@remote:~# tree /opt/remote_shift/
/opt/remote_shift/
├── kafka
│   ├── Dockerfile
│   ├── param_run_container.sh
│   └── run_image.sh
│ 
└── zookeeper
│   ├── Dockerfile
│   ├── param_run_container.sh
│   └── run_image.sh
│
.
.
.
└── n-th service
    ├── Dockerfile
    ├── param_run_container.sh
    └── run_image.sh

```





