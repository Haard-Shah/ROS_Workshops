# %% Step 4a

import sys

import rospy
from geometry_msgs.msg import PoseStamped

import moveit_commander
from moveit_commander.move_group import MoveGroupCommander
from moveit_commander.planning_scene_interface import PlanningSceneInterface

# we'll look closer at this soon
from poses import ORIGIN_POSE, BASKETBALL_POSE, BASKETBALL_GRASP_POSE, DUNK_IN_HOOP_POSE

# initialize the ros node
moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('slam_dunk_node')

# publish the target Poses in RViz so we can visualize our motion goals
target_pose = rospy.Publisher(
    "target_pose", PoseStamped, queue_size=10, latch=True)

# %% Step 4b

# create moveit interface objects
robot_arm = MoveGroupCommander('slam_dunk_planning_group')

# MoveIt computes trajectories somewhat non-deterministically.
# Our obstacle course is quite challenging; so lets give it some more time to work with
robot_arm.set_planning_time(5)
robot_arm.set_num_planning_attempts(10)

# %% Step 4c

environment = PlanningSceneInterface(synchronous=True)
# let moveit know what objects are in the robot's environment.
# note that these are usually dynamic objects; static objects such as the environment
# are typically defined as a "link" in the urdf.xacro
environment.add_mesh('environment', ORIGIN_POSE, "environment.stl",
                     size=(0.01, 0.01, 0.01))
environment.add_mesh('basketball', BASKETBALL_POSE, "basketball.stl",
                     size=(0.2, 0.2, 0.2))

# %% Step 4d


def move_to_pose(pose: PoseStamped):
    # publish the goal so that we can see it in rviz
    target_pose.publish(pose)

    # calculate a JointTrajectory "plan" that could be followed to reach the target
    robot_arm.set_pose_target(pose.pose)
    success, plan, _, _ = robot_arm.plan()
    assert success

    # now execute the planned path.
    # this should always succeed as our robot is simulated and will do exactly what we command!
    success = robot_arm.execute(plan, wait=True)
    assert success

# %% Step 4e


print("Moving to BASKETBALL_GRASP_POSE")
move_to_pose(BASKETBALL_GRASP_POSE)

robot_arm.attach_object('basketball')

try:
    print("Moving to DUNK_IN_HOOP_POSE")
    move_to_pose(DUNK_IN_HOOP_POSE)

finally:
    robot_arm.detach_object('basketball')

print("MJ got nothin' on me")

moveit_commander.roscpp_shutdown()
