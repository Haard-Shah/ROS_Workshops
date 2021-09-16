from std_msgs.msg import Header
from geometry_msgs.msg import PoseStamped, Pose, Point, Quaternion


def define_pose(position, quaternion):
    return PoseStamped(
        header=Header(frame_id="world"),
        pose=Pose(
            position=Point(*position),
            orientation=Quaternion(*quaternion)
        )
    )


# define important poses for our robot task wrt. the "world" frame / the ORIGIN
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
