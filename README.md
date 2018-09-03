# mu3

<i> in progress </i>

<i> Details on how it works in below Muie fig. </i>

```
                                                  /
+-----------------------+                         | blueprint_run_container.sh
| /opt/local_blueprint/ |----[folder contains]----|
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
                            +-------------------------+                           | Dockerfile 
                            | /opt/local_shift/kafka  |----[folder now contains]--| param_run_container.sh
                            +-------------------------+                           | run_image.sh
                                      ||                                          \ 
                                      ||                                          
                                      ||                                          /
                            +-------------------------+                           | Dockerfile 
                            |/opt/local_shift/zookeep.|----[folder now contains]--| param_run_container.sh
                            +-------------------------+                           | run_image.sh
                                      ||                                          \
                                      ||
                                      ||                                
                        /// lots of others image ///
                        ///     containers...    ///

                \                                                                                      /
                 \----------------------------------------\/------------------------------------------/
                                                          ||
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
                                                          ||
                                                +-------------------------+          |
                                                | /opt/remote_shift/kafka |----------| building images &containers
                                                +-------------------------+          | 
                                                          || 
                                                          ||
                                                          ||
                                                +-------------------------+          |
                                                | /opt/remote_shift/zooke.|----------| building images &containers
                                                +-------------------------+          |
                                                          ||
                                                          ||
                                                ///lots of other images///
                                                /// and containers     ///
                                                ///  to build...       ///

```
<i> Fig. Muie </i>
