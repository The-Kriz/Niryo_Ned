from pyniryo import *
from Ned_Constants import *
from pyniryo.vision import *

def robotStart():
    """
    Connect to the robot through ip address
    Connect the tool
    Auto_calibrate
    :return: Client
    """
    # Connect to robot
    Client = NiryoRobot(Robot_Ip_Address)
    # Changing tool
    Tool_Used = NiryoRobot.get_current_tool_id(Client)
    Client.update_tool()
    # Calibrate robot if robot needs calibration
    Client.calibrate_auto()
    Client.wait(Robot_Sleep)
    Client.move_to_home_pose()
    return Client

def robotStop(Client):
    """
    Stops & Disconnect the robot
    :param Client: Robot
    :return: NONE
    """
    # Ending
    Client.go_to_sleep()
    # Releasing connection
    Client.close_connection()

def cellAddressPos(Cell_Address):
    """
    gets the *Cell_Address* and assign the Board_place_pose_cell PoseObject
    :param Cell_Address: cell number to place the box
    :return: Board_place_pose_cell PoseObject
    """
    print(Cell_Address[0])
    if Cell_Address[0] == 0:
        if Cell_Address[1] == 0:
            placeCellPose = Board_place_pose_cell_00
        elif Cell_Address[1] == 1:
            placeCellPose = Board_place_pose_cell_01
        elif Cell_Address[1] == 2:
            placeCellPose = Board_place_pose_cell_02

    elif Cell_Address[0] == 1:
        if Cell_Address[1] == 0:
            placeCellPose = Board_place_pose_cell_10
        elif Cell_Address[1] == 1:
            placeCellPose = Board_place_pose_cell_11
        elif Cell_Address[1] == 2:
            print("1 2")
            placeCellPose = Board_place_pose_cell_12
            print(placeCellPose)

    elif Cell_Address[0] == 2:
        if Cell_Address[1] == 0:
            placeCellPose = Board_place_pose_cell_20
        elif Cell_Address[1] == 1:
            placeCellPose = Board_place_pose_cell_21
        elif Cell_Address[1] == 2:
            placeCellPose = Board_place_pose_cell_22

    return placeCellPose

def robotPlaceOnCell(Client,Cell_Address):
    """
    Moves to *Pick_From_Tray*
    picks the Box
    moves to *Board_Observation_Pose*
    Place the box in the cell
    moves to *Board_Observation_Pose*
    :param Client: Robot
    :param Cell_Address: cell number to place the box
    :return:
    """
    Client.wait(Robot_Sleep)
    Client.pick_from_pose(Pick_From_Tray)
    Client.wait(Robot_Sleep)
    Client.move_pose(Board_Observation_Pose)
    Client.wait(Robot_Sleep)
    placeCellPose = cellAddressPos(Cell_Address)
    Client.place_from_pose(placeCellPose)
    Client.wait(Robot_Sleep)
    Client.move_pose(Board_Observation_Pose)
    Client.wait(Robot_Sleep)

def robotGameCellReset(Client):
    """
    finds all the Blocks
    picks all Robot_Block one by one
        place it in *Place_To_Tray*
    picks all Human_Block one by one
        place it in *Place_To_Tray*

    :param Client:
    :return:
    """
    Client.move_pose(Board_Observation_Pose)
    Client.wait(Robot_Sleep)

    while True:
        object_found, object_pose, object_shape, object_color = Client.detect_object(Robot_Workspace,
                                                                         shape=Robot_Block_Shape,
                                                                         color=Robot_Block_Colour)
        if obj_found:
            if object_shape == Robot_Block_Shape_Str or object_color == Robot_Block_Colour_Str :
                Client.pick_from_pose(object_pose)
                Client.wait(Robot_Sleep)
                Client.place_from_pose(Place_To_Tray)
                Client.wait(Robot_Sleep)
        else:
            break

        Client.move_pose(Board_Observation_Pose)
        Client.wait(Robot_Sleep)

    while True:
        object_found, object_pose, object_shape, object_color = Client.detect_object(Robot_Workspace,
                                                                         shape=Human_Block_Shape,
                                                                         color=Human_Block_Colour)
        if obj_found:
            if object_shape == Human_Block_Shape_Str or object_color == Human_Block_Colour_Str :
                Client.pick_from_pose(object_pose)
                Client.wait(Robot_Sleep)
                Client.place_from_pose(Place_To_Human_Tray)
                Client.wait(Robot_Sleep)
        else:
            break

        Client.move_pose(Board_Observation_Pose)
        Client.wait(Robot_Sleep)

def robotBackHome(Client):
    """
    Moves the robot back to Home
    :param Client:
    :return:
    """
    Client.move_to_home_pose()

def robotObservationPose(Client):
    """
    Moves to the Observation_Pose
    :param Client:
    :return:
    """
    Client.move_pose(Board_Observation_Pose)

def turnOnLearningMode(Client):
    """
    Turns on the Training Mode
    :param Client:
    :return:
    """
    Client.move_to_home_pose()
    Client.set_learning_mode(True)

def turnOffLearningMode(Client):
    """
    Turns on the Training Mode
    :param Client:
    :return:
    """
    Client.set_learning_mode(False)
    Client.move_to_home_pose()
















































# def positionCordinates(Image,MaskColour, MaskReturn = False):
#     hsv_img = cv2.cvtColor(Image, cv2.COLOR_BGR2HSV)
#     mask = cv2.inRange(hsv_img, MaskColour[0], MaskColour[1])
#     contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     for contour in contours:
#         M = cv2.moments(contour)
#     if M["m00"] != 0:
#         center_x = int(M["m10"] / M["m00"])
#     center_y = int(M["m01"] / M["m00"])
#     cv2.circle(img, (center_x, center_y), 5, (0, 255, 0), -1)
#     if MaskReturn == True:
#         return center_x, center_y, mask
#     else:
#         return center_x,center_y











