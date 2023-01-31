from pyniryo import *

robot_ip_address = "10.10.10.10"   #add ip address

# Connect to robot & calibrate
robot = NiryoRobot(robot_ip_address)
robot.calibrate_auto()
# Move joints
robot.move_joints(0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
# Turn learning mode ON
robot.set_learning_mode(True)
# Stop TCP connection
robot.close_connection()

