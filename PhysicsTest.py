import Physics as ph 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

# earth = ph.Particle(mass=5.972*(10**24), position=np.array([6371, 0]), velocity=np.array([0, 0]))
# sun = ph.Particle(mass=1.989*(10**30), position=np.array([0, 0]), velocity=np.array([0, 0]))
# time_stepper = ph.TimeStepper()
p1 = ph.Particle()
p2 = ph.Particle(position=np.array([10, 0]))

r_vec = p2.position - p1.position    # Determines the displacement vector from this Particle to the other_particle
r = np.linalg.norm(r_vec)                          # Finds the magnitude of the displacement vector
r_norm = (1 / r) * r_vec                           # Finds the normal direction vector of the displacement

p2.force = - 5 * r_norm

p2.initOrbit(p1)

x = []
y = []

for i in range(1, 10):
    p2.position = p2.position + (p2.velocity * 0.001)
    p2.velocity = p2.velocity + ((p2.force / p2.mass) * 0.001)
    p2.force = -5 * r_norm
    x.append(p2.position[0])
    y.append(p2.position[1])