import Physics as ph 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

particle_1 = ph.Particle(mass=1, position=np.array([0, 5]), velocity=np.array([0, 0]))
particle_2 = ph.Particle(mass=1, position=np.array([0, 0]), velocity=np.array([0, 0]))
time_stepper = ph.TimeStepper()

for particle in ph.Particle.particles:
    particle.calcGravitationalPull()

particle_1.initOrbit(particle_2)

x = []
y = []

for i in range(1, 10000):
    time_stepper.step()
    x.append(particle_2.position[0])
    y.append(particle_2.position[1])

plt.scatter(x, y)
plt.show() 