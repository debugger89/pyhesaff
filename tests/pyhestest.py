from __future__ import absolute_import, print_function, division
import __sysreq__  # NOQA
# Standard
import sys
from os.path import realpath, join, dirname
import vtool
# Scientific
import numpy as np
import cv2
# TPL
import pyhesaff


def load_test_data(short=False, n=0, **kwargs):
    if not 'short' in vars():
        short = False
    # Read Image
    #ellipse.rrr()
    nScales = 4
    nSamples = 16
    img_fname = 'zebra.jpg'
    if '--test.png' in sys.argv:
        img_fname = 'jeff.png'
    if '--zebra.png' in sys.argv:
        img_fname = 'zebra.jpg'
    if '--lena.png' in sys.argv:
        img_fname = 'lena.jpg'
    img_fpath = realpath(join(dirname(vtool.__file__), 'tests', 'testdata', img_fname))
    imgBGR = cv2.imread(img_fpath)
    imgLAB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2LAB)
    imgL = imgLAB[:, :, 0]
    detect_kwargs = {
        'scale_min': 20,
        'scale_max': 100
    }
    detect_kwargs.update(kwargs)
    kpts, desc = pyhesaff.detect_kpts(img_fpath, **detect_kwargs)
    if short and n > 0:
        extra_fxs = []
        if img_fname == 'zebra.png':
            extra_fxs = [374, 520, 880][0:1]
        fxs = np.array(spaced_elements2(kpts, n).tolist() + extra_fxs)
        kpts = kpts[fxs]
        desc = desc[fxs]
    test_data = locals()
    return test_data


def spaced_elements2(list_, n):
    if n is None:
        return np.arange(len(list_))
    if n == 0:
        return np.empty(0)
    indexes = np.arange(len(list_))
    stride = len(indexes) // n
    return indexes[0:-1:stride]


def spaced_elements(list_, n):
    if n is None:
        return 'list'
    indexes = np.arange(len(list_))
    stride = len(indexes) // n
    return list_[indexes[0:-1:stride]]
