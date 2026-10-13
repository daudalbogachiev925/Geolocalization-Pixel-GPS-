import numpy as np
from src.camera_model import CameraModel
from src.geo import pixel_to_gps

def test_center_pixel_maps_to_drone_position():
    cam = CameraModel(1000, 1000, 960, 540, 1920, 1080)
    lat, lon = pixel_to_gps(cam, 960, 540, 100, 0, -1.5708, 0, 55.75, 37.61)
    assert abs(lat - 55.75) < 0.001
    assert abs(lon - 37.61) < 0.001
