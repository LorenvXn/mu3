
<i> In Progress </i>

<br>

<i>Requirements: make sure Jupyter has a Python 3 kernel</i>

<br>

Ansible (infrastructure) code is re-written using Python3. 

All changes that involve <b> extra-vars </b> option are done by passing a <b> json </b> as argument:

 </br>
From the usual ansible playbook with extra-vars (the usual way):

```
ansible-playbook zookeeper.yaml --extra-vars "containername=zooky, [...etc...] "
````
...to python &json:

```
python zookeeper.py "{\"containername\" : \"zooky\", [...etc...] }" 
```

