from pyniryo import *

sensor_pin_id = PinID.GPIO_1A

catch_nb = 3

# The pick pose
pick_pose = PoseObject(
    x=0.269, y=-0.023, z=0.12,
    roll=1.232, pitch=1.569, yaw=1.257,
)
# The Place pose
place_pose = PoseObject(
                     x=0.021, y=-0.238, z=0.122,
                      roll=0.121, pitch=1.523, yaw=-1.46)
# -- MAIN PROGRAM

# Connecting to the robot
robot = NiryoRobot("169.254.200.200")

# Activating connexion with the Conveyor Belt
conveyor_id = robot.set_conveyor()

for i in range(catch_nb):
    robot.run_conveyor(conveyor_id)
    while robot.digital_read(sensor_pin_id) == PinState.HIGH:
        robot.wait(0)

    # Stopping robot's motor
    robot.stop_conveyor(conveyor_id)
    # Making a pick & place
    robot.pick_and_place(pick_pose, place_pose)

# Deactivating connexion with the Conveyor Belt
robot.unset_conveyor(conveyor_id)