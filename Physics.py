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

    def initOrbit(self, particle):
        '''Calculates the initial velocity required for the orbit of this particle about another'''
        r_vector = self.position - particle.position 
        r_scalar = np.linalg.norm(r_vector)
        F_scalar = np.linalg.norm(self.force)

        F_x = self.force[0]
        F_y = self.force[1]
                
        v_scalar = np.sqrt((F_scalar * r_scalar) / self.mass)
        v_norm = np.array([-np.sqrt((F_y ** 2) / (F_x ** 2 + F_y ** 2)), np.sqrt(((F_x ** 2) / ((F_x ** 2) + (F_y ** 2))))])
        v_vector = v_scalar * v_norm   

        self.velocity = v_vector



class TimeStepper:
    '''A class that updates the properties of Bodies using a Newtonian method'''

    def __init__(self, delta_t=0.001):
        self.delta_t = delta_t 
    
    def step(self):
        '''A method that updates the properties of the particles after some time delta_t has passed'''
        for particle in Particle.particles:
            particle.position = particle.position + particle.velocity * self.delta_t 
            particle.velocity = particle.velocity + (particle.force / particle.mass) * self.delta_t 
            particle.calcGravitationalPull()
            
            
