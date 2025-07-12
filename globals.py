import sys
from os import path

"""get the directory of the current script or executable"""
def get_current_directory():
    if getattr(sys, "frozen", False):
        return path.join(path.dirname(sys.executable), '_internal')
    elif __file__:
        return path.join(path.dirname(__file__))
    else:
        return path.abspath('.')

