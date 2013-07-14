import numpy as np
import matplotlib.pyplot as plt

def integrate(r,h,dr):
    # S = 0.0
    n = len(h)
    print n
    B = np.zeros((1,n-1))
    for i in range(1,len(r)):
        B[0,i-1] = h[i-1]-h[i] 

    C = np.multiply(np.pi,np.power(r,2))
    S = np.dot(B,C[1:])


    return S[0]

def get_xmax(theta):
    v0 = 20.0
    g = 9.81
    xmax = .5*np.sin(2.*theta)*(v0**2)*(1./g)
    return xmax


def compute_path(x,theta):
    # theta in radians
    v0 = 20.0
    g = 9.81
    y0 = 100.0
    x2 = np.power(x,2)
    A1 = -0.5*g*(1/v0**2)
    y = y0 + np.multiply(x,np.tan(theta))
    y = y + A1*(1/(np.power(np.cos(theta),2)))*x2
    return y

def get_theta(x):
    v0 = 20.0
    g = 9.81
    theta = np.arctan(np.divide((v0**2),g*x))
    return theta

def frange(start,stop,step):
    x = start
    if start < stop:
        while x < stop:
            yield x
            x += step
        return
    else:
        while x > stop:
            yield x
            x += step
        return
        

def solve_improved():
    v0 = 20.0
    g = 9.81
    y0 = 100.0
    A1 = -0.5*g*(1/v0**2)
    for dx in [1e-2,1e-3,1e-4]:
        S = 0.0
        x = dx
        theta = get_theta(x)
        yprev = compute_path(x,theta)
        while True:
            x += dx
            x2 = np.power(x,2)

            theta = get_theta(x)
            y = y0 + np.multiply(x,np.tan(theta))
            y = y + A1*(1/(np.power(np.cos(theta),2)))*x2

            if y < 0.0:
                print 'y < 0 at x = ' + str(x)
                break
            S += (yprev-y)*np.pi*np.power(x,2)
            yprev = y
        print (dx,S)
    

def solve_integral():
    a = 1e-5
    b = 99.0834
    v0 = 20.0
    g = 9.81
    y0 = 100.0
    a2 = np.power(a,2)
    b2 = np.power(b,2)
    vo2 = np.power(v0,2)
    
    Fb = 0.25*np.pi*b2*(-g*b2/vo2 + 2.*vo2/g + 4*y0)
    Fa = 0.25*np.pi*a2*(-g*a2/vo2 + 2.*vo2/g + 4*y0)
    print Fb
    print Fa
    return Fb-Fa

def find_max_distance():
    dx = 1e-5
    v0 = 20.0
    g = 9.81
    y0 = 100.0
    x = np.arange(98.5, 101, dx)

    maxx = 0
    miny = float('inf')
    for deg in frange(22.1,22.4,.01):
        theta = np.radians(deg)
        y = compute_path(x,theta)
        for i in range(0,len(y)):
            if y[i] < 0.0: 
                 break
            if x[i] > maxx:
                    maxx = x[i]
                    max_theta = theta


    # y = compute_path(x,max_theta)
    # plt.plot(x,y)
    # plt.show()
    print (maxx,np.degrees(max_theta))



if __name__ == "__main__":
    # ans = find_max_distance();
    ans = solve_integral()
    print "**************"
    print ans

