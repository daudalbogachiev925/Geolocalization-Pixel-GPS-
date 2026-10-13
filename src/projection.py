import numpy as np
from src.camera_model import CameraModel
from src.gimbal import rotation_matrix

EARTH_RADIUS = 6378137.0

def project_to_ground(cam: CameraModel, u, v, altitude,
                      yaw, pitch, roll):
    ray_cam = np.array(cam.pixel_to_ray(u, v))
    R = rotation_matrix(yaw, pitch, roll)
    ray_world = R @ ray_cam
    if ray_world[2] >= 0:
        return None
    t = -altitude / ray_world[2]
    point_body = ray_world * t
    return point_body  # [north, east, down]

def body_to_geo(point_body, lat0, lon0):
    north, east, _ = point_body
    dlat = north / EARTH_RADIUS * 180 / np.pi
    dlon = east / (EARTH_RADIUS * np.cos(np.radians(lat0))) * 180 / np.pi
    return lat0 + dlat, lon0 + dlon
