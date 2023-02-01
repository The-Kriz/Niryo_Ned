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
    # Pick
    robot.pick_from_pose(pick_pose)
    # Place
    robot.place_from_pose(place_pose)

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
