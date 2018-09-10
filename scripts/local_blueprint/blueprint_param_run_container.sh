#!/bin/bash

docker create -i -t  --name namecontainer -p porthost:portcontainer   \
--storage-opt size=amountgb \
--cap-add=ALL  `docker images | grep tagimage | awk {'print $3'} | grep -vi image` /bin/bash

sleep 5

docker start namecontainer
