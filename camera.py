import cv2

def get_camera(index=0):
    """Returns a VideoCapture object for the given camera index."""
    return cv2.VideoCapture(index)
