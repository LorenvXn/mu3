# mu3

<i> in progress </i>

<b> Ship a containerized architecture with the help of Ansible 2.6 </b>... <i>because mă-ta! ¯\\_(ツ)_/¯ </i>

<b>Note:</b>
```
My apologies to the outsiders for the (somewhat) brvtal 2pac lyrics as comments, 
but this "project-sketch" was required by some corporate folks who have no good manners, 
and these folks step on self-learners as if nothing wrong could ever happen to them.
(It wasn't actually required, they have no idea what they are doing. I just crafted this approach!)

You know that saying: "Ballz is life!" ... well, not in a corporation, bruh! 
What to be expected from educated "men". /shrugs
``` 


If you are asking yourselves why I did not bother with the usual directories (default, tasks, roles, meta) ...    
well, it's a very boring and corporate approach, and I am a big fan of chaos.


Whatevs! Onto the presentation... 

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



