from pyniryo import *


Robot_Ip_Address = "169.254.200.200" # Robot's ip address

Robot_Workspace = "workspace_1" # Robot's Workspace

Robot_Sleep = 2 #seconds
Gripper_Tool_Speed = 500 #Tool gripper speed
Max_Board_Pick_Count = 9


#Objects
Circle_Block = ObjectShape.CIRCLE
Square_Block = ObjectShape.SQUARE
Red_Block = ObjectColor.RED
Blue_Block = ObjectColor.BLUE
Green_Block = ObjectColor.GREEN

Robot_Block_Shape = ObjectShape.SQUARE
Robot_Block_Shape_Str = "SQUARE"
Robot_Block_Colour = ObjectColor.BLUE
Robot_Block_Colour_Str = "BLUE"

Human_Block_Shape = ObjectShape.CIRCLE
Human_Block_Shape_Str = "CIRCLE"
Human_Block_Colour = ObjectColor.RED
Human_Block_Colour_Str = "RED"

#PoseObjects ////////////////////////////////////////////////////////////////////////////////////////

Home = PoseObject(
                    x=0.30, y=0.0, z=0.15,
                    roll=0, pitch=1.57, yaw=0.0,
                    )


Pick_From_Tray = PoseObject(
    x=0.218, y=0.258, z=0.134,
roll = 2.162, pitch = 1.078, yaw = 2.132

                         )

"""
    x=0.2222, y=0.2643, z=0.1405,
roll = 2.251, pitch = 1.124, yaw = 2.127
"""
"""    x=0.214, y=0.265, z=0.135,
roll = 2.243, pitch = 1.122, yaw = 2.212"""
""""""

Place_To_Tray = PoseObject(
                            x=0.30, y=0.0, z=0.15,
                            roll=0, pitch=1.57, yaw=0.0,
                            )

Place_To_Human_Tray = PoseObject(
                                x=0.30, y=0.0, z=0.15,
                                roll=0, pitch=1.57, yaw=0.0,
                            )

# Pick_From_Board = PoseObject(
#                             x=0.30, y=0.0, z=0.15,
#                             roll=0, pitch=1.57, yaw=0.0
#                             )


Board_Observation_Pose = PoseObject(
                                    x=-0.0178, y=-0.1092, z=0.4264,
                                    roll = -0.114, pitch = 1.444, yaw = -1.732
                                    )

# Place Pose for each cell on the board
Board_place_pose_cell_00 = PoseObject(
                                        x=0.0346, y=-0.3194, z=0.0965,
                                        roll = -0.305, pitch = 1.561, yaw = -1.856
                                    )

Board_place_pose_cell_01 = PoseObject(
                                        x = -0.0186, y = -0.3207, z = 0.0966,
                                        roll = -0.190, pitch = 1.500, yaw = -1.686
                                    )

Board_place_pose_cell_02 = PoseObject(
                                        x = -0.0686, y = -0.3132, z = 0.0972,
                                        roll = -0.316, pitch = 1.486, yaw = -1.840
                                    )

Board_place_pose_cell_10 = PoseObject(
                                        x = 0.0363, y = -0.2656, z = 0.0964,
                                        roll = -3.015, pitch = 1.562, yaw = 1.703
                                    )

Board_place_pose_cell_11 = PoseObject(
                                        x = -0.0167, y = -0.2657, z = 0.0965,
                                        roll = 3.135, pitch = 1.560, yaw = 1.561
                                    )

Board_place_pose_cell_12 = PoseObject(
                                        x = -0.0631, y = -0.2595, z = 0.0963,
                                        roll = -0.257, pitch = 1.544, yaw = -1.828
                                    )

Board_place_pose_cell_20 = PoseObject(
                                        x = 0.0425, y = -0.2022, z = 0.0956,
                                        roll = 0.171, pitch = 1.543, yaw = -1.373
                                    )

Board_place_pose_cell_21 = PoseObject(
                                        x = -0.0101, y = -0.1969, z = 0.0957,
                                        roll = -0.079, pitch = 1.558, yaw = -1.642

                                    )

Board_place_pose_cell_22 = PoseObject(
                                        x = -0.0573, y = -0.1899, z = 0.0959,
                                        roll = -0.326, pitch = 1.535, yaw = -1.870
                                    )







""" 
Board_place_pose_cell_00 = x = 0.0346, y = -0.3194, z = 0.0965
roll = -0.305, pitch = 1.561, yaw = -1.856 
 Board_place_pose_cell_01 = x = -0.0186, y = -0.3207, z = 0.0966
roll = -0.190, pitch = 1.500, yaw = -1.686 
 Board_place_pose_cell_02 = x = -0.0686, y = -0.3132, z = 0.0972
roll = -0.316, pitch = 1.486, yaw = -1.840 
 Board_place_pose_cell_10 = x = 0.0363, y = -0.2656, z = 0.0964
roll = -3.015, pitch = 1.562, yaw = 1.703 
 Board_place_pose_cell_11 = x = -0.0167, y = -0.2657, z = 0.0965
roll = 3.135, pitch = 1.560, yaw = 1.561 
 Board_place_pose_cell_12  = x = -0.0631, y = -0.2595, z = 0.0963
roll = -0.257, pitch = 1.544, yaw = -1.828 
 Board_place_pose_cell_20  = x = 0.0425, y = -0.2022, z = 0.0956
roll = 0.171, pitch = 1.543, yaw = -1.373 
 Board_place_pose_cell_21 = x = -0.0101, y = -0.1969, z = 0.0957
roll = -0.079, pitch = 1.558, yaw = -1.642 
 Board_place_pose_cell_22 = x = -0.0573, y = -0.1899, z = 0.0959
roll = -0.326, pitch = 1.535, yaw = -1.870 
"""

"""

findMarkers : 
480 640 3
True
findMarkers : 
480 640 3
workSpaceImageTrim : 
200 200 3

"""