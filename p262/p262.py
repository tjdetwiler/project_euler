import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import axes3d


def get_surface(X,Y):

    z = np.ndarray(shape=(X.size,Y.size))
    for i in range(0,X.size):
        for j in range(0,Y.size):
            x = X[i]
            y = Y[j]
            z[i,j] = (5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) )*np.exp(-1.*np.abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7))

    return z

def fun(x,y):
            return (5000-0.005*(x*x+y*y+x*y)+12.5*(x+y) )*np.exp(-1.*np.abs(0.000001*(x*x+y*y)-0.0015*(x+y)+0.7))


def solve():

    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')

    xs = ys = np.arange(0,1600,25)
    X,Y = np.meshgrid(xs,ys)
    Z = get_surface(xs,ys)

    print X.shape
    print Y.shape
    print Z.shape


    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm,
                         linewidth=0, antialiased=False)


    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()        


    
def solve2():
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.1)
    print X.shape
    print Z.shape
    ax.scatter(X, Y, Z)

    plt.show()

    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    #     plt.draw()



if __name__== "__main__":
  start = time.time()
  ans = solve()
  print "**************"
  print ans
  stop = time.time()
  print "runtime: " + str(stop-start)
