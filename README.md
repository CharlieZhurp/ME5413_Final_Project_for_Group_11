# ME5413_FINAL_PROJECT for Group 11  

Authors: CHEN JUNJIE, THONG CHEE WAI,BENJAMIN, YI ZHENG, ZHU RUIPENG

## Reference:  

Cartographer Official documents:  
https://google-cartographer-ros.readthedocs.io/en/latest/index.html  
ME5413_Final_Project Official documents:  
https://github.com/NUS-Advanced-Robotics-Centre/ME5413_Final_Project  
SC-Aloam Official documents:  
https://github.com/gisbi-kim/SC-A-LOAM  

##### You can also install and build in your workspace according to official documents.

## Dependencies

### System Requirements:

    Ubuntu 20.04 (18.04 not yet tested)
    ROS Noetic (Melodic not yet tested)
    C++11 and above
    CMake: 3.0.2 and above
    
### This repo depends on the following standard ROS pkgs:

    roscpp
    rospy
    rviz
    std_msgs
    nav_msgs
    geometry_msgs
    visualization_msgs
    tf2
    tf2_ros
    tf2_geometry_msgs
    pluginlib
    map_server
    gazebo_ros
    jsk_rviz_plugins
    jackal_gazebo
    jackal_navigation
    velodyne_simulator
    teleop_twist_keyboard

And this gazebo_model repositiory  

## Installation   

    cd  
    git clone  
    cd ME5413_Final_Project   

### This is the final project for Group 11, containing three sub-workspace.
#### 1. Cartographer_ws:

    #Build
    catkin_make_isolated --install --use-ninja
    #Source
    source install_isolated/setup.bash
    #Start Cartographer
    roslaunch cartographer_ros demo_my_robot.launch bag_filename:=/path/to/your_bag.bag

#### 2.ME5413_Final_Project:
 
    #Build  
    catkin_make  
    
    #Source  
    source devel/setup.bash  
    
    #Launch Gazebo World together with our robot  
    roslaunch me5413_world world.launch  
    
    #Only launch the robot keyboard teleop control  
    roslaunch me5413_world manual.launch  
    
    #Launch GMapping  
    roslaunch me5413_world mapping.launch  
    
    #Save the map as `my_map` in the `maps/` folder  
    roscd me5413_world/maps/    
    rosrun map_server map_saver -f my_map map:=/map  
    
    #Load a map and launch localizer  
    roslaunch me5413_world navigation_teb.launch  

#### 3.sc_aloam_ws

    #Build  
    catkin_make  
    
    #Source
    source devel/setup.bash  
    
    #Start SC-ALOAM  
    roslaunch aloam_velodyne aloam_mulran.launch   


