

Proceed with following steps:


1) Install docker  (after updating the system, right? right!)
```
apt-get install docker.io </b>
```

2) Format new disk  (let's say /dev/sdb, shall we?) to xfs:

```
sudo mkfs.xfs /dev/sdb
```

3) Mount it (it must have pquota as an option)

```
mkdir /blah
mount -o discard,defaults,pquota /dev/sdb /blah
```
3.1) If you forgot to add pquota option just modity /etc/fstab 

```
[...]
UUID=blahblah-000blablah-someid  /blah xfs discard,defaults,pquota 0 0

```

3.2) Then,  unmount & mount:
```
umount /blah
mount /blah

```
Magic!

4) Stop docker service

```
service docker stop
```

5) Configure overlay2 storage driver:
a) Create daemon.json
```
touch /etc/docker/daemon.json
```
and add following content:

```
{
  "storage-driver": "overlay2"
}
```

5.1) start service docker just to check the service can be brought up without errors

```
service docker start 
```

6) Stop docker again

```
service docker stop
```

7) Time to move and symlink the docker files to new /blah

```
mkdir /blah/data
chmod a+w /blah/data
 ```
 
```
mv /var/lib/docker /blah/data
ln -s /blah/data /var/lib/docker
```
8) Start docker service, and make sure there are no errors:

```
service docker start
```

9) Check if everything is alright:
```
root@wildhost#docker info | grep -iE 'storage driver|backing filesystem'
Storage Driver: overlay2
 Backing Filesystem: xfs
```
```
ls -ltr /var/lib/docker
lrwxrwxrwx 1 root root 13 Sep  6 11:27 /var/lib/docker -> /blah/data/
```

10) Create a container just get wild about the storage option:

```
root@wildhost:~# docker run -it --storage-opt size=3G ubuntu /bin/bash
Unable to find image 'ubuntu:latest' locally
[...]
Status: Downloaded newer image for ubuntu:latest
root@bedbed263:/# df -h /
Filesystem      Size  Used Avail Use% Mounted on
overlay         3.0G  8.0K  3.0G   1% /
```
Noice!


