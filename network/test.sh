#!/bin/bash

#you run this after containers creation..dah!
#you provide the hosts IP on which services were deployed, & not the containers IP
# dah!

CONTAINER=$1
KAFKA_IP=$2
ZOO_IP=$3

#testing - testing -----------------------
#docker exec $CONTAINER ls
#lol! such 1337 skillz ... thanks, port forwarding!

docker exec $CONTAINER \
sed -i 's/#advertised/advertised/g;s/your.host.name/'"$KAFKA_IP"'/g;s/localhost/'"$ZOO_IP"'/g' \
/opt/kafka/config/server.properties 

