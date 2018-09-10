

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
