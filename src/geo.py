from src.camera_model import CameraModel
from src.projection import project_to_ground, body_to_geo

def pixel_to_gps(cam, u, v, altitude, yaw, pitch, roll, lat0, lon0):
    p = project_to_ground(cam, u, v, altitude, yaw, pitch, roll)
    if p is None:
        return None
    return body_to_geo(p, lat0, lon0)
