<b> Ship a containerized architecture with the help of Ansible 2.6 </b>
(<i> still working on it... </i>)

> Make sure the content from scripts will be under /opt folder on master host

<br>
<br>

<i> Bonus: </i> Now, you can easily ship it with Ansible Python3 API: [Python 3 and Jupyter](https://github.com/LorenvXn/mu3/tree/master/Jupyter_approach)

<br>
<b> a) How the Ansible approach does work: </b>

```

		   +-----------------------------+
		   |			         |
		   |   Blueprint of scripts      |
		   |	and Dockerfiles          |
		   |			         |	
	           +--------------+--------------+	
				  |
				  |
				  |
			          |
		   +-----------------------------+
		   |			         |
		   |  Conditional main.yaml      |   	 
		   |     entire flow depends     |
		   |     on the image name       |
                   +--------------+--------------+
				  | 
				  |
				  |
				  |
 +--------------------------------------------------------------------+
 |    user can choose the storage amount,remote host IP, tag image,   |
 |                             port host,    			      | 
 |                port container, and name container                  |
 +--------------------------------------------------------------------+
			          |	
				  |
				  |
   +------------------------------+------------------------------+
   |			          |			         |
   |			          |			         |
   +------------+		  +------------+.                +------------+
   | image  A   | 	  . . .   | image Y    |	         | image Z    |  
   +------------+		  +------------+                 +------------+
   |			          |			         |
   |- container a1   . . .        |- container y1                |- container z1 
   |- container a2   . . .	  |- container y2                |- container z2
   .			          .			         .
   .                              .			         .
   .			          .			         .
   |- container an   . . .	  |- container yn	         |- container zn



```

</br> 

For more details on scripts flow, check the diagram: [Diagram Flow](https://github.com/LorenvXn/mu3/blob/master/flow.txt) 

</br> 

<b> b) Storage approach </b>

OverlayFS approach for persistance  - check [Storage - HowTo](https://github.com/LorenvXn/mu3/blob/master/storage/HowTo.md) for more details

</br> 
<b> c) Folders ierarchy </b>


 
<b> c.1) Folders ierarchy on master host </b>

Folder <b>/opt</b> contains the following: 
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

Subfolder <b> /opt/local_blueprint </b> contains the blueprint scripts of services

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

Subfolder  <b> /opt/local_shift </b> contains the modified scripts of services,
that will be copied to remote hosts:

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

Subfolder <b> /opt/play </b> contains the ansible playbooks:

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

<b> c.2) Folders ierarchy on remote hosts </b>


Subfolder <b> /opt/remote_shift </b> contains the the modified &copied scripts from master host (/opt/local_shift location).
The deployment of the services will be done from the ansible playbooks, as well. 

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


<i> Networking approach - soon </i> 


