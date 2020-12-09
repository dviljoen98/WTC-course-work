from turtle import *
import random
import turtle

obstacles_list = []


def generate_obstacles():
    """
    This function generates the walls of the maze using multiple for loops.
    """
    global obstacles_list
    for x in range(-68,80,4):
        obstacles_list.append((x,161))
    for y in range(-165,163,4):
        obstacles_list.append((-84,y))
    for y in range(-160,163,4):
        obstacles_list.append((77,y))
    for x in range(-80,63,4):
        obstacles_list.append((x,-165))
    for y in range(-135,130,4):
        obstacles_list.append((55,y))
    for x in range(-80,56,4):
        obstacles_list.append((x,128))
    for y in range(-130,130,4):
        obstacles_list.append((-65,y))
    for x in range(-50,55,4):
        obstacles_list.append((x,-135))
    for y in range(-100,83,4):
        obstacles_list.append((-45,y))
    for x in range(-45,30,4):
        obstacles_list.append((x,100))
    for y in range(-100,103,4):
        obstacles_list.append((30,y))
    for x in range(-65,30,4):
        obstacles_list.append((x,-100))
    for y in range(-68,63,4):
        obstacles_list.append((10,y))
    for x in range(-20,12,4):
        obstacles_list.append((x,60))
    for y in range(-55,62,4):
        obstacles_list.append((-20,y))
    for x in range(-8,12,4):
        obstacles_list.append((x,-68))
    for x in range(-42,-20,4):
        obstacles_list.append((x,-30))
    
    return obstacles_list


def get_obstacles():
    """
    Gets the randomly generated obstacles from the function in the return
    """
    return generate_obstacles()


def is_position_blocked(x,y):
    """
    This function checks if the robots postion falls inside an obstacle coordinate
    and returns True if the position is blocked by an obstacle
    """
    global obstacles_list
    for i in obstacles_list:
        if i[0] <= x <= i[0]+4 and i[1] <= y <= i[1]+4:
            return True
    return False


def is_path_blocked(x1,y1, x2, y2):
    """
    This function checks if there is an obstacle in the line between the random x and y coordinate
    and returns True if there is an obstacle in that line
    """
    global obstacles_list

    if x1 > x2:
        x1,x2 = x2,x1
    
    if y1 > y2:
        y1,y2 = y2,y1

    if x1==x2:
        for y in range(y1,y2+1):
            if is_position_blocked(x1,y):
                return True

    if y1==y2:
        for x in range(x1,x2+1):
            if is_position_blocked(x,y1):
                return True

    return False

    