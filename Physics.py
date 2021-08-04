import tkinter 
import numpy as np 

class Particle:
    '''A class to model the properties and behaviours of physical bodies'''
    particles = []

    def __init__(self, mass=1, position=np.array([0, 0]), velocity=np.array([0, 0])):
        self.mass = mass 
        self.position = position 
        self.velocity = velocity 
        self.force = np.array([0, 0]) 

        Particle.particles.append(self)


class TimeStepper:
    '''A class that updates the properties of Bodies using a Newtonian method'''

    def __init__(self, delta_t=0.001):
        self.delta_t = delta_t 
    
    
