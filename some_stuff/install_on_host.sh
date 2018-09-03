##########################################################
# not containers related
# some bash functions to install on a host kafka service
# it also makes the necessary changes on the host
############################
# for those who still use/read bash... ;) 
###############


#!/bin/bash


if [ ! -d /opt/zookeeper/conf ]; then
  mkdir -p /opt/zookeeper/conf ;
fi

if [ ! -d /opt/kafka ]; then
  mkdir -p /opt/kafka ;
fi



declare -a install_steps=(  install_updates \
                            python_installation \
                            install_java \
                            install_zookeeper \
                            install_kafka \
			                      modify_zookeeper_host \
			                      modify_host_file
                         )
                        
 
install_updates()
 {
  apt-get update 
  apt-get install -y --no-install-recommends apt-utils &&\
  apt-get update &&\
  apt-get install -y curl vim wget iproute2
 }
 
 
python_installation() 
{ 

  curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
                                        python get-pip.py && \
                                        pip install celery kafka-python Flask
  apt-get update -y
} 


install_java()
{
  echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | \
  tee -a /etc/apt/sources.list && \
  echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" | \
  tee -a /etc/apt/sources.list && \
  echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true| \
  /usr/bin/debconf-set-selections && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886 && \
  apt-get update && apt-get install -y curl dnsutils oracle-java8-installer ca-certificates
} 

install_zookeeper()
{
  wget -q -O - http://mirror.csclub.uwaterloo.ca/apache/zookeeper/zookeeper-3.4.10/zookeeper-3.4.10.tar.gz | \
  tar -xzf - -C /opt \
  && mv /opt/zookeeper-3.4.10 /opt/zookeeper \
  && cp /opt/zookeeper/zookeeper-3.4.10/conf/zoo_sample.cfg /opt/zookeeper/conf/zoo.cfg
}

install_kafka()
{
  wget http://archive.apache.org/dist/kafka/0.10.0.1/kafka_2.11-0.10.0.1.tgz && \
  tar xvzf kafka_2.11-0.10.0.1.tgz && \
  mv kafka_2.11-0.10.0.1  kafka
}


#if you have to deal
#with a useless cr4p like Cloud environment

modify_zookeeper_host()
{
  IP=`ifconfig eth0 | perl -nle'/t addr:(\S+)/&&print$1'`
  sed -i "s/localhost/$IP/g" /opt/kafka/kafka_2.11-0.10.0.1/config/server.properties
}


modify_host_file()
{
  H=`hostname`
  L=127.0.0.1
  sed  -i  "2i $L $H" /etc/hosts
}


for z in "${install_steps[@]}"
do
        $z
done
