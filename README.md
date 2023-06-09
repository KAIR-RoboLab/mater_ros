# mater_ros

ROS 2 Humble packages used for mater robot. Work together with MicroROS [mater_firmware](https://github.com/KAIR-RoboLab/mater_firmware).

## Install

``` bash
mkdir ros2_ws
cd ros2_ws
git clone https://github.com/KAIR-RoboLab/mater_ros src/mater_ros
vcs import src < src/mater_ros/mater/mater.repos

rosdep update --rosdistro $ROS_DISTRO
rosdep install -i --from-path src --rosdistro $ROS_DISTRO -y
colcon build
```

## Changing ROS_DOMAIN_ID

To change ROS_DOMAIN_ID you are using run
``` bash
export ROS_DOMAIN_ID=my_awesome_domain_id
```
Replace `my_awesome_domain_id` with number from 0 do 254. Don't forget to match the domain id with one in the firmware. Check [mater_firmware](https://github.com/KAIR-RoboLab/mater_firmware) for more information.

## Run

In order to launch all 

``` bash
ros2 launch mater_bringup bringup.launch.py
```

If running robot with display attached you can run:

``` bash
ros2 launch mater_bringup bringup.launch.py rviz:=true
```

If you want only to launch RViz2 run:
``` bash
ros2 launch mater_bringup rviz.launch.py
```

If you robot is connected to different serial port use command:
``` bash
ros2 launch mater_bringup bringup.launch.py serial_port:=/dev/ttyMY_SERIAL_PORT
```

## ROS interface

### Publishes

- `/joint_states` [*sensor_msgs/JointState*]: state of wheel joints.
- `/mater/odom` [*nav_msgs/Odometry*]: odometry from wheels.
- `/odometry/filtered` [*nav_msgs/Odometry*]: filtered odometry from EKF.


### Subscribes

- `/cmd_vel` [*geometry_msgs/Twist*]: commanded velocity.
