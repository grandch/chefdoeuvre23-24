import numpy as np
import math

def get_target_position(camera_position, direction_vector):
    direction_vector_normalized = direction_vector / np.linalg.norm(direction_vector)
    return camera_position + 1 * direction_vector_normalized

def spherical_to_rectangular_coord(theta, phi):
    theta = theta * (math.pi / 180)
    phi = phi * (math.pi / 180)
    x = math.sin(phi) * math.cos(theta)
    y = math.sin(phi) * math.sin(theta)
    z = math.cos(phi)
    return [x,y,z]


print("Target:", get_target_position([.4124579436349758, 0.058085583954402234, -0.33230771606359427], [0.7069253626303624, -0.0050278319727824535, -0.70727028254804]))
print("Up:", spherical_to_rectangular_coord(45,0))
print("Target:", get_target_position([-0.26187965706737165, 0.0639193905312978, -0.3371195109510675], [-0.7050955373549855, 0.021399258609251473, -0.7073998022650063]))
print("Up:", spherical_to_rectangular_coord(45,180))
print("Target:", get_target_position([0.07629510952287223, 0.06160241046937788, -0.4743865210065597], [0.00010022446694059381, 0.0022486489440108944, -0.99999746676320828]))
print("Up:", spherical_to_rectangular_coord(0,180))
print("Target:", get_target_position([-0.04723309843906157, 0.06267489306727239, -0.45902214575013506], [-0.2585864044438378, 0.00788600190483143, -0.9659559422557641]))
print("Up:", spherical_to_rectangular_coord(15,180))
print("Target:", get_target_position([0.1995977351808692, 0.06094895876798736, -0.4572594416582021], [0.2587834110929345, -0.0008224308213560734, -0.965935023565586]))
print("Up:", spherical_to_rectangular_coord(15,180))
