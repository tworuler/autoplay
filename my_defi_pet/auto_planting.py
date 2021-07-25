#!/usr/bin/env python
# coding: utf-8

import logging
import os
import time
import pyautogui
import numpy as np

logging.basicConfig(format='[%(asctime)s %(filename)s:%(lineno)d %(levelname)s] %(message)s', level=logging.INFO)


def find_image(path):
    position = pyautogui.locateOnScreen(path, 0.8)
    print(position)
    if position is None:
        return None
    center = pyautogui.center(position)
    return center


def get_land_position():
    pos = (841, 544)
    return pos


def get_window_offset():
    pos = np.array((260, 180))
    return pos


def get_window_center():
    size = np.array((930, 480))
    return get_window_offset() + size / 2


def click(pos):
    x, y = pos
    print(f'click ({x}, {y})')
    pyautogui.moveTo(x, y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.2)


def gain_corn():
    # manually click last land first

    first_land_pos = get_window_offset() + (405, 295)
    click(first_land_pos)
    time.sleep(1)

    land_pos = get_window_center() + (0, 10)
    land_pos_offsets = np.array([(-30, -15), (65, 0), (-35, -10), (65, 0)])
    for offset in land_pos_offsets:
        pos = land_pos + offset
        click(pos)
        time.sleep(0.5)

    click(first_land_pos)
    time.sleep(1)


def plant_corn():
    pos = get_window_offset() + (770, 200)
    for i in range(5):
        click(pos)
    return


def main():
    print('Start...')
    click(get_window_offset())
    while True:
        gain_corn()
        plant_corn()
        time.sleep(63)


if __name__ == '__main__':
    main()
