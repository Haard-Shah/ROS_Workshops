# QUT ROS Workshop 4: MoveIt! Slam DUNK

![final product in rviz](./dunk.png "Slam Dunk!")

## Setup

```bash
sudo apt install ros-melodic-moveit python-catkin-tools
source /opt/ros/melodic/setup.sh
catkin build
```

## Running The Script

```bash
source devel/setup.sh
roslaunch slam_dunk_moveit_config demo.launch
```

And in another terminal:

```bash
source devel/setup.sh
python3 slam_dunk.py
```

## Workshop Instructions

Backup and remove the `slam_dunk_moveit_config` folder:

```bash
mv src/slam_dunk_moveit_config slam_dunk_moveit_config.bak
```

Run MoveIt! Setup Assistant:

```bash
source devel/setup.sh
roslaunch moveit_setup_assistant setup_assistant.launch
```

TODO!: detailed setup_assistant instructions

Run the demo launch and test moving the arm around in an empty environment:

```bash
roslaunch slam_dunk_moveit_config demo.launch
```

TODO!: detailed slam_dunk.py coding instructions
