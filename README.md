# mu3

<i> in progress </i>

<i> Details on how it works in below Muie fig. </i>

```
                                                  /
+-----------------------+                         | blueprint_run_container.sh
| /opt/local_blueprint/ -----[folder contains]----|
+-----------------------+                         | blueprint_run_image.sh
                                                  \
\                                                                                /
 \------------------------------------\/----------------------------------------/
                                      ||
                                      ||
                                      ||
                [[                                              ]]
                [[     modify and copy blueprints locally       ]]
                [[             to /opt/local_shift              ]]
                                      ||
                                      ||
                                      ||                                          
                                      ||                                          /     
                            +-------------------------+                           | param_run_container.sh
                            | /opt/local_shift/kafka  -----[folder now contains]--| 
                            +-------------------------+                           | run_image.sh
                                      ||                                          \ 
                                      ||                                          
                                      ||                                           /
                            +--------------------------+                           | param_run_container.sh
                            |/opt/local_shift/zookeeper-----[folder now contains]--| 
                            +--------------------------+                           | run_image.sh
                                      ||                                           \
                                      ||
                                      ||                                
                        /// lots of others image ///
                        ///     containers...    ///

                \                                                                                      /
                 \----------------------------------------\/------------------------------------------/
                                                          ||
                                                          ||
                                                          ||
                                          [[     copy Dockerfiles from      ]]       
                                          [[       /opt/local_images/       ]]
                                          [[      to /opt/remote_shift/     ]] 
                                                          ||
                                                          ||
                                                          ||
                                           [[                               ]]
                                           [[copy everything to remote hosts]]
                                           [[ under /opt/remote_shift/      ]]
                                           [[       ...and build :)         ]]
                                           [[                               ]]
                                                          ||
                                                          ||
                                                          ||
                                                          ||
                                                          ||    
                                                          ||                                          /
                                                +-------------------------+                          | Dockerfile
                                                | /opt/remote_shift/kafka ---[folder contains]-------| run_image.sh
                                                +-------------------------+                          | param_run_container.sh
                                                          ||              |                           \
                                                          ||              |
                                                          ||              |
                                                          ||              |          |
                                                          ||              +----------| building images &containers
                                                          ||.                        | 
                                                          ||                                           /
                                              +---------------------------+                           | Dockerfile
                                              |/opt/remote_shift/zookeeper----[folder contains]-------| run_image.sh
                                              +---------------------------+                           |param_run_container.sh
                                                          ||              |                            \
                                                          ||              |
                                                          ||              |
                                                          ||              |           | 
                                                          ||               +----------| building images &containers
                                                          ||                          |
                                                          ||
                                                ///lots of other images///
                                                /// and containers     ///
                                                ///  to build...       ///

```
<i> Fig. Muie </i>
