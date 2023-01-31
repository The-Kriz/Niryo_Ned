from pyniryo import *

robot = NiryoRobot("10.10.10.10")

robot.calibrate_auto()

# Moving Joints with function & 6 floats
robot.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)

# # Moving Joints with function & a list of floats
# robot.move_joints([-0.5, -0.6, 0.0, 0.3, 0.0, 0.0])
#
# # Moving Joints with setter & 6 floats
# robot.joints = 0.2, -0.4, 0.0, 0.0, 0.0, 0.0
#
# # Moving Joints with setter & a list of floats
# robot.joints = [-0.2, 0.3, 0.2, 0.3, -0.6, 0.0]

# Getting Joints with function
joints_read = robot.get_joints()

# j1, j2, j3, j4, j5, j6 = robot.get_joints()

# pose_target_obj = PoseObject(0.2, 0.0, 0.2, 0.0, 0.0, 0.0)
# robot.move_pose(pose_target_obj)



pick_pose = PoseObject(
x=0.30, y=0.0, z=0.15,
roll=0, pitch=1.57, yaw=0.0
)
first_place_pose = PoseObject(
    x=0.0, y=0.2, z=0.15,
    roll=0, pitch=1.57, yaw=0.0
)
for i in range(5):
    robot.move_pose(pick_pose)
    new_place_pose = first_place_pose.copy_with_offsets(x_offset=0.05 * i)
    robot.move_pose(new_place_pose)




robot.release_with_tool()
