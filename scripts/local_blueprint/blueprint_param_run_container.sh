#!/bin/bash

docker create -i -t --name containername -p porthost:portcontainer \
--cap-add=ALL  `docker images | grep tagimage | awk {'print $3'} | grep -vi image` /bin/bash

sleep 5

docker start containername
