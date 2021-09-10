# QUT ROS Workshop 4

## MoveIt! Slam Dunk

Install deps and setup workspace:

```bash
sudo apt install ros-melodic-moveit python-catkin-tools
source /opt/ros/melodic/setup.sh
catkin build
source devel/setup.sh
```

Run MoveIt! Setup Assistant:

```bash
roslaunch moveit_setup_assistant setup_assistant.launch
catkin build
```

Run the demo launch and test setting target poses manually:

```bash
roslaunch
```
