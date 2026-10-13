from dataclasses import dataclass

@dataclass
class CameraModel:
    fx: float
    fy: float
    cx: float
    cy: float
    width: int
    height: int

    def pixel_to_ray(self, u, v):
        return ((u - self.cx) / self.fx, (v - self.cy) / self.fy, 1.0)
