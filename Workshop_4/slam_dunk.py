import sys
from typing import Iterable
from moveit_commander import robot

import rospy
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

import moveit_commander
from moveit_commander.move_group import MoveGroupCommander
from moveit_commander.planning_scene_interface import PlanningSceneInterface

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('slam_dunk_node')

robot_arm = MoveGroupCommander('slam_dunk_planning_group')

target_pose = rospy.Publisher(
    "target_pose", PoseStamped, queue_size=10, latch=True)

environment = PlanningSceneInterface(synchronous=True)


def define_pose(position: Iterable[float], quaternion: Iterable[float]):
    return PoseStamped(
        header=Header(
            frame_id="world"
        ),
        pose=Pose(
            position=Point(*position),
            orientation=Quaternion(*quaternion)
        )
    )


# define important poses wrt. the "world" frame
ORIGIN_POSE = define_pose(
    [0, 0, 0],
    [0, 0, 0, 1]
)
BASKETBALL_POSE = define_pose(
    [0.4468396053, -0.0034719435, 0.3678862186],
    [0, 0, 0, 1]
)
BASKETBALL_GRASP_POSE = define_pose(
    [0.3871681929, 0.0200828641, 0.4057507893],
    [0.0843928720, 0.8555283434, -0.1217124127, 0.4961201321]
)
DUNK_IN_HOOP_POSE = define_pose(
    [-0.3412968401, -0.0248166078, 0.3888232048],
    [-0.4673231353, -0.8836860646, -0.0240147086, -0.0114595050]
)

environment.add_mesh('environment', ORIGIN_POSE, "environment.stl",
                     size=(0.01, 0.01, 0.01))
environment.add_mesh('basketball', BASKETBALL_POSE, "basketball.stl",
                     size=(0.2, 0.2, 0.2))

# MoveIt computes trajectories somewhat non-deterministically.
# Our obstacle course is quite challenging; so lets give it some more time to work with
robot_arm.set_planning_time(10)
robot_arm.set_num_planning_attempts(10)


rospy.sleep(0.5)  # sleep so targets.publish() works


def move_to_pose(pose: PoseStamped):
    # publish the goal so that we can see it in rviz
    target_pose.publish(pose)

    # calculate a path that could be followed to reach the
    robot_arm.set_pose_target(pose.pose)
    success, plan, _, _ = robot_arm.plan()
    assert success

    # now execute the planned path.
    # This should always succeed as our robot is simulated and will do exactly what we command!
    success = robot_arm.execute(plan, wait=True)
    assert success


print("Moving to BASKETBALL_GRASP_POSE")
move_to_pose(BASKETBALL_GRASP_POSE)

robot_arm.attach_object('basketball')

try:
    print("Moving to SLAM DUNK")
    move_to_pose(DUNK_IN_HOOP_POSE)

finally:
    robot_arm.detach_object('basketball')

print("MJ got nothin' on me")

moveit_commander.roscpp_shutdown()
