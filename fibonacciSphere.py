import math, random

def fibonacci_sphere(samples=1,randomize=True):
    rnd = 1.
    if randomize:
        rnd = random.random() * samples

    points = []
    offset = 2./samples
    increment = math.pi * (3. - math.sqrt(5.));

    for i in range(samples):
        y = ((i * offset) - 1) + (offset / 2);
        r = math.sqrt(1 - pow(y,2))

        phi = ((i + rnd) % samples) * increment

        x = math.cos(phi) * r
        z = math.sin(phi) * r

        points.append([x,y,z])

    return points

from numpy import pi, cos, sin, arccos, arange
import mpl_toolkits.mplot3d
import matplotlib.pyplot as pp
def sunflowerSphere():
    num_pts = 1000
    indices = arange(0, num_pts, dtype=float) + 0.5

    phi = arccos(1 - 2*indices/num_pts)
    theta = pi * (1 + 5**0.5) * indices

    x, y, z = cos(theta) * sin(phi), sin(theta) * sin(phi), cos(phi);

    pp.figure().add_subplot(111, projection='3d').scatter(x, y, z);
    pp.show()

from numpy import pi, cos, sin, sqrt, arange
import matplotlib.pyplot as pp
def sunflowerSpiral():
    num_pts = 1000
    indices = arange(0, num_pts, dtype=float) + 0.5

    r = sqrt(indices/num_pts)
    theta = pi * (1 + 5**0.5) * indices

    pp.scatter(r*cos(theta), r*sin(theta))
    pp.show()

sunflowerSphere()
