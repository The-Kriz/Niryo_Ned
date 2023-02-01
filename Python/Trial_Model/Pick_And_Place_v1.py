# Imports
from pyniryo import *

tool_used = ToolID.XXX  # Tool used for picking
robot_ip_address = "ip address" # Robot address

# The pick pose
pick_pose = PoseObject(
    x=0.25, y=0., z=0.15,
    roll=-0.0, pitch=1.57, yaw=0.0,
)
# The Place pose
place_pose = PoseObject(
    x=0.0, y=-0.25, z=0.1,
    roll=0.0, pitch=1.57, yaw=-1.57)

def pick_n_place_version(robot):
    height_offset = 0.05  # Offset according to Z-Axis to go over pick & place poses
    gripper_speed = 400

    # Going Over Object
    robot.move_pose(pick_pose.x, pick_pose.y, pick_pose.z + height_offset,
                               pick_pose.roll, pick_pose.pitch, pick_pose.yaw)
    # Opening Gripper
    robot.open_gripper(gripper_speed)
    # Going to picking place and closing gripper
    robot.move_pose(pick_pose)
    robot.close_gripper(gripper_speed)

    # Raising
    robot.move_pose(pick_pose.x, pick_pose.y, pick_pose.z + height_offset,
                               pick_pose.roll, pick_pose.pitch, pick_pose.yaw)

    # Going Over Place pose
    robot.move_pose(place_pose.x, place_pose.y, place_pose.z + height_offset,
                               place_pose.roll, place_pose.pitch, place_pose.yaw)
    # Going to Place pose
    robot.move_pose(place_pose)
    # Opening Gripper
    robot.open_gripper(gripper_speed)
    # Raising
    robot.move_pose(place_pose.x, place_pose.y, place_pose.z + height_offset,
                               place_pose.roll, place_pose.pitch, place_pose.yaw)

if __name__ == '__main__':
    # Connect to robot
    client = NiryoRobot(robot_ip_address)
    # Calibrate robot if robot needs calibration
    client.calibrate_auto()
    # Changing tool
    client.update_tool()

    pick_n_place_version(client)

    # Releasing connection
    client.close_connection()
