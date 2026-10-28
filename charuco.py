import os
import numpy as np
import cv2
import constants


def create_and_save_new_board():
    dictionary = cv2.aruco.getPredefinedDictionary(constants.ARUCO_DICT)
    board = cv2.aruco.CharucoBoard((constants.SQUARES_VERTICALLY, constants.SQUARES_HORIZONTALLY), constants.SQUARE_LENGTH, constants.MARKER_LENGTH, dictionary)
    size_ratio = constants.SQUARES_HORIZONTALLY / constants.SQUARES_VERTICALLY
    img = cv2.aruco.CharucoBoard.generateImage(board, (constants.LENGTH_M, int(constants.LENGTH_M*size_ratio)), marginSize=constants.MARGIN_M)
    cv2.imshow("img", img)
    cv2.waitKey(2000)
    cv2.imwrite(constants.SAVE_NAME, img)

create_and_save_new_board()