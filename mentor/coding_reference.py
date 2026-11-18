"""Public mentor reference for the basic elastic-particle exercise.
This file is not imported by the student notebooks.
"""
import numpy as np

def move(position, velocity, dt):
    return position + velocity * dt

def wall(position, velocity):
    if position < 0:
        position = -position
        velocity = -velocity
    elif position > 1:
        position = 2 - position
        velocity = -velocity
    return position, velocity

def my_simulation(x, y, vx, vy, dt, steps):
    frames = [[x,y]]
    for step in range(steps):
        x = move(x, vx, dt)
        y = move(y, vy, dt)
        x, vx = wall(x, vx)
        y, vy = wall(y, vy)
        frames.append([x,y])
    return np.array(frames)
