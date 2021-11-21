from pylab import rc
from sympy.plotting import plot3d
from sympy.abc import x,y
rc('font',size=16)
rc('text',usetex=True)
z=((1 - x** 2 / 8 - y ** 2 / 10) * 6)
plot3d(z,(x,-10,10),(y,-10,10),xlabel='$x$',ylabl='$y$')
