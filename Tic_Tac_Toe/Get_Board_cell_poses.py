from Ned_Retry import *

robot = robotStart()
turnOnLearningMode(robot)
input("Move to Pose Then Press Enter to Save...")
# Place Pose for each cell on the board
Board_place_pose_cell_00 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_01 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_02 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_10 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_11 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_12 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_20 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_21 = pose_read = robot.get_pose()
input("Move to Pose Then Press Enter to Save...")
Board_place_pose_cell_22 = pose_read = robot.get_pose()
turnOffLearningMode(robot)
robotStop(robot)
input("All Pos Done Printing Pos...")
print(f" Board_place_pose_cell_00 = {Board_place_pose_cell_00} \n Board_place_pose_cell_01 = {Board_place_pose_cell_01} \n Board_place_pose_cell_02 = {Board_place_pose_cell_02} \n Board_place_pose_cell_10 = {Board_place_pose_cell_10} \n Board_place_pose_cell_11 = {Board_place_pose_cell_11} \n Board_place_pose_cell_12  = {Board_place_pose_cell_12} \n Board_place_pose_cell_20  = {Board_place_pose_cell_20} \n Board_place_pose_cell_21 = {Board_place_pose_cell_21} \n Board_place_pose_cell_22 = {Board_place_pose_cell_22} ")




