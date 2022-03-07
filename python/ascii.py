#!/usr/bin/env python3

import cv2
import imutils
import os

from math import floor


def convert(vc_frame):
    h, w = frame.shape[0:2]

    density_chars = "Ñ@#W$9876543210?!abc;:+=-,._                                   "
    # density_chars = "_.,-=+:;cba!?0123456789$W#@Ñ   "
    density_chars_len = len(density_chars)
    pixel_index_count = 0

    string_buffer = []
    clear_console()
    for column in vc_frame:
        for pixel in column:
            average_colour = sum(pixel) / len(pixel)  # Getting the average value from the RBG values

            density_index = floor((average_colour * density_chars_len) / 255)
            string_buffer.append(density_chars[density_index - 1])

            if pixel_index_count == w - 1:
                print("".join(string_buffer))
                string_buffer.clear()
                pixel_index_count = 0
                continue

            pixel_index_count += 1
            

def clear_console():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


if __name__ == "__main__":

    # Generic video capture stuff
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        # Generic video capture stuff
        rval, frame = vc.read()
        cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        frame = imutils.resize(frame, width=100)
        cv2.imshow("preview", frame)

        # Handle exit
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break

        # parse video data
        convert(frame)

    # Clean up
    vc.release()
    cv2.destroyWindow("preview")
