import Physics as ph 
import numpy as np 

particle_1 = ph.Particle(mass=1, position=np.array([0, 5]), velocity=np.array([0.1, 0]))
particle_2 = ph.Particle(mass=1, position=np.array([0, 0]), velocity=np.array([0, 0]))

for particle in ph.Particle.particles:
    particle.calcGravitationalPull()

for particle in ph.Particle.particles:
    print(particle.force)

