import sys

import rospy
from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion

import moveit_commander
from moveit_commander.move_group import MoveGroupCommander
from moveit_commander.planning_scene_interface import PlanningSceneInterface

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('slam_dunk')

ORIGIN = PoseStamped(
    header=Header(
        frame_id="world"
    ),
    pose=Pose(
        position=Point(0, 0, 0),
        orientation=Quaternion(0, 0, 0, 1)
    )
)

environment = PlanningSceneInterface()
# MUST SLEEP. PlanningSceneInterface's implementation requires this;
# otherwise the add_mesh function below will be ignored.
# Why? Your guess is as good as mine.
rospy.sleep(2)
environment.add_mesh('obstacles', ORIGIN, "environment.stl",
                     size=(0.01, 0.01, 0.01))

robot_arm = MoveGroupCommander('slam_dunk')

# our obstacle course is quite challenging! We need to give moveit a bit of extra time.
# robot_arm.set_planning_time(20)
robot_arm.set_num_planning_attempts(10)

# just above the hoop
HOOP = PoseStamped(
    header=Header(
        frame_id="world"
    ),
    pose=Pose(
        position=Point(-0.3475245233, -0.0232578443, 0.3682473160),
        orientation=Quaternion(-0.9986380939, -0.0345536632,
                               -0.0390896358, 0.0000472383)
    )
)
BASKETBALL = PoseStamped(
    header=Header(
        frame_id="world"
    ),
    pose=Pose(
        position=Point(0.4468396053, -0.0034719435, 0.3728862186),
        orientation=Quaternion(-0.9982654178, 0.0565203398,
                               0.0164763244, 0.0003709629)
    )
)

targets = rospy.Publisher("targets", PoseStamped, queue_size=10)
rospy.sleep(0.5)  # sleep so targets.publish() works

targets.publish(BASKETBALL)
robot_arm.set_pose_target(BASKETBALL.pose)
success, plan, _, _ = robot_arm.plan()
assert success

# now execute the planned path.
# This should always succeed as our robot is simulated and will do exactly what we command!
success = robot_arm.execute(plan, wait=True)
assert success

targets.publish(HOOP)
robot_arm.set_pose_target(HOOP.pose)
success, plan, _, _ = robot_arm.plan()
assert success

# now execute the planned path.
# This should always succeed as our robot is simulated and will do exactly what we command!
success = robot_arm.execute(plan, wait=True)
assert success

moveit_commander.roscpp_shutdown()
