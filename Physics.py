import tkinter 
import numpy as np 


class Constants:
    '''A class to contain physical constants'''
    G = 6.67408 * (10 ** (-11))


class Particle:
    '''A class to model the properties and behaviours of physical bodies'''
    particles = []

    def __init__(self, mass=1, position=np.array([0, 0]), velocity=np.array([0, 0])):
        self.mass = mass 
        self.position = position 
        self.velocity = velocity 
        self.force = np.array([0, 0]) 

        Particle.particles.append(self)

    def calcGravitationalPull(self):
        '''
        This method calculates the gravitational attraction between this instance of Particle and all 
        other Partical instances in Particle.particles and then modifies the force property of those
        OTHER Particals accordingly. 
        '''
        for other_particle in Particle.particles:
            if self != other_particle:
                r_vec = other_particle.position - self.position    # Determines the displacement vector from this Particle to the other_particle
                r = np.linalg.norm(r_vec)                          # Finds the magnitude of the displacement vector
                r_norm = (1 / r) * r_vec                           # Finds the normal direction vector of the displacement

                force = - (Constants.G * self.mass * other_particle.mass) / (r ** 2)
                force_vec = force * r_norm 

                other_particle.force = other_particle.force + force_vec



class TimeStepper:
    '''A class that updates the properties of Bodies using a Newtonian method'''

    def __init__(self, delta_t=0.001):
        self.delta_t = delta_t 
    
    
