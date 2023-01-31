# Imports
from pyniryo import *

tool_used = ToolID.XXX  # Tool used for picking
robot_ip_address = "x.x.x.x" # Robot address

# The pick pose
pick_pose = PoseObject(
    x=0.25, y=0., z=0.15,
    roll=-0.0, pitch=1.57, yaw=0.0,
)
# The Place pose
place_pose = PoseObject(
    x=0.0, y=-0.25, z=0.1,
    roll=0.0, pitch=1.57, yaw=-1.57)

def pick_n_place_version_2(robot):
    height_offset = 0.05  # Offset according to Z-Axis to go over pick & place poses

    pick_pose_high = pick_pose.copy_with_offsets(z_offset=height_offset)
    place_pose_high = place_pose.copy_with_offsets(z_offset=height_offset)

    # Going Over Object
    robot.move_pose(pick_pose_high)
    # Opening Gripper
    robot.release_with_tool()
    # Going to picking place and closing gripper
    robot.move_pose(pick_pose)
    robot.grasp_with_tool()
    # Raising
    robot.move_pose(pick_pose_high)

    # Going Over Place pose
    robot.move_pose(place_pose_high)
    # Going to Place pose
    robot.move_pose(place_pose)
    # Opening Gripper
    robot.release_with_tool(gripper_speed)
    # Raising
    robot.move_pose(place_pose_high)

    
if __name__ == '__main__':
    # Connect to robot
    client = NiryoRobot(robot_ip_address)
    # Calibrate robot if robot needs calibration
    client.calibrate_auto()
    # Changing tool
    client.update_tool()

    pick_n_place_version_x(client)

    # Releasing connection
    client.close_connection()