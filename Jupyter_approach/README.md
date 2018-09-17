
<i> In Progress </i>

<br>

<i>Requirements: make sure Jupyter has a Python 3 kernel</i>

<br>

Ansible (infrastructure) code is re-written using Python3

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

<b>Or, just use a json file.</b>



<i> snip code can be successfully applied to the brief example (test_py3)</i>
</br>
<i> Just modify the code before passing the data to variable_manager as extra_vars. </i>
</br>
```
[...snip...]
#data=json.loads(sys.argv[1])

filename="/home/hehe/hehe.json"
jj=open(filename, 'r')
confile=jj.read()
data = json.loads(confile)
[...snip...]
```
<i> where hehe.json contains line:</i>  { "weather" : "news" }
 </br>
 
 
<b> Brief Example </b></br>
Check [test_py3](https://github.com/LorenvXn/mu3/blob/master/Jupyter_approach/test_py3.ipynb) for a brief example - it deploys changes on a known file,</br>
by  using modules shell (for cat) and regexp (for word replacement). 


<b>Why re-writing it? </b>

This approach will allow the user to run changes from master node,</br>
just by using the jupyter notebooks. No need for terminals. 
