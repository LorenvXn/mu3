# mu3

<i> in progress </i>

<b> Ship a containerized architecture with the help of Ansible 2.6 </b>... <i>because mă-ta! ¯\\_(ツ)_/¯ </i>

<i> Details on the process flow of the scripts in below Muie fig. </i>

```
                                                  /
+-----------------------+                         | blueprint_run_container.sh
| /opt/local_blueprint/ -----[folder contains]----|
+-----------------------+                         | blueprint_run_image.sh
                                                  \
\                                                                                /                   (I.)
 \------------------------------------\ /----------------------------------------/ 
                                       |
                                       |
                                       |
                                       ▼ 
               [[                                              ]]
   X◄----------[[     modify and copy blueprints locally       ]]
   |           [[             to /opt/local_shift              ]]
   |                                 
   | 
   |
   |                                                                               /
   ▼                        +-------------------------+                           | param_run_container.sh
   X-----------------------►| /opt/local_shift/kafka  -----[folder now contains]--| 
   |                        +-------------------------+                           | run_image.sh
   |                                                                               \ 
   |                                                                             
   |                                                                                /
   ▼                        +--------------------------+                           | param_run_container.sh
   X-----------------------►|/opt/local_shift/zookeeper-----[folder now contains]--| 
   |                        +--------------------------+                           | run_image.sh
   |                                                                                \
   |
 [...] 
   |
   ▼
   X-----------------------► ///   lots of others image ///
                             ///  containers scripts    ///

      \                                                                                                /  (II.)
       \---------------------------------------------\ /-----------------------------------------------/
                                                      |
                                                      |
                                                      |
                                                      ▼ 
                                   [[     copy Dockerfiles from      ]]       
                                   [[       /opt/local_images/       ]]
                                   [[      to /opt/remote_shift/     ]] 
                                                      |
                                                      |
                                                      |                                                   (III.)
                                                      ▼ 
                                   [[                                      ]]
                                   [[copy everything from /opt/local_shift ]]
                      +◄-----------[[      under /opt/remote_shift/        ]]
                      |            [[            ...and build :)           ]]
                      |            [[                                      ]]
                      |                            
                      |                            
                      |                            
                      |                                                                               /
                      ▼                         +-------------------------+                          | Dockerfile
                      X------------------------►| /opt/remote_shift/kafka ---[folder contains]-------| run_image.sh
                      |                         +-------------------------+                          | param_run_container.sh
                      |                                                   |                           \
                      |                                                   |
                      |                                                   |
                      |                                                   |           |
                      |                                                   +---------->| building images &containers
                      |                                                               | 
                      |                                                                                /
                      ▼                       +---------------------------+                           | Dockerfile
                      X----------------------►|/opt/remote_shift/zookeeper----[folder contains]-------| run_image.sh
                      |                       +---------------------------+                           |param_run_container.sh
                      |                                                   |                            \
                      |                                                   |
                      |                                                   |
                      |                                                   |           | 
                      |                                                   +---------->| building images &containers
                      |                                                               |
                      |                                      
                      ▼                         ///lots of other images///
                      X-----------------------► /// and containers     ///
                                                ///  to build...       ///

```
<i> Fig. Muie </i>

(I.) + (II.) - process flow that takes place on local (master) host 
<br>
(III.) - process flow that takes place on remote host(s)



