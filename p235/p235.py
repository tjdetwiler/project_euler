import numpy as np
import matplotlib.pyplot as plt
import time

N = 5000
A0 = {}
A1 = {}
A2 = {}
tt = 1

def sn(r):
    k = 1
    s = 0
    while k <= N:
      u = (900-3*k)*r**(k-1)
      s += u
      k += 1
    return s + 6e11

def get_X(r):
  X = np.zeros(N);
  for i in range(0,len(X)):
      X[i] = r**(N-1-i)
  return X

# function coefficients
def get_A0():
  k = range(1,N+1);
  A0 = [900-3*x for x in k] 
  A0 = np.array(A0[::-1])
  A0[len(A0)-1] += int(6e11)
  return A0

# gradient coefficients 
def get_A1(A0):
  A1 = np.zeros(N)
  i = 1
  while i < len(A0):
    A1[i] = (N-i)*A0[i-1]
    i += 1 
  return A1

# hessian coefficients
def get_A2(A1):
  A2 = np.zeros(N)
  i = 2
  while i < len(A1):
    A2[i] = (N-i)*A1[i-1]
    i += 1
  return A2


def set_coefficient_vectors():
  global A0
  global A1
  global A2
  A0 = get_A0()
  A1 = get_A1(A0)
  A2 = get_A2(A1)  

def fr(r):
    f0 = fx(get_X(r))
    return f0 - (1./tt)*np.log(f0)   

def fx(X):
    f0 = np.dot(A0,X)
    return f0 - (1./tt)*np.log(f0)   

def Dfx(X):
    f0 = np.dot(A0,X)
    df0 = np.dot(A1,X)
    return df0 + (-1./tt)*(1./f0)*df0

def Hfx(X):
    f0 = np.dot(A0,X)
    df0 = np.dot(A1,X)
    hf0 = np.dot(A2,X)
    return  hf0 + (1. / tt) * (1. / (f0**2)) * (df0**2) + (-1. / f0) * hf0

def get_lambda_sq(f,D,H):
    return D*(1./H)*D;

# backtracking line search
def get_step_size(r,dr):
    t = 1
    alpha = .1
    beta = .6
    X = get_X(r)
    f = fx(X)
    D = Dfx(X)
    while True:
      lower_bound = fr(r+t*dr)
      upper_bound = f + alpha*t*D*dr
      if lower_bound <= upper_bound:
          return t
      t = beta*t      
     
def plot_some():
   set_coefficient_vectors()
   x = []
   y = []
   for k in range(0,30):
     x.append(1.0023+k*.00001)
    
   t = 50
   for r in x:
    f = sn(r) + 6e11
    y.append(f)

   plt.plot(x,y)
   plt.show()


def newtons_method():

  r = 1.00232
  max_dr = 1e-13
  old_r = 0
  
  while True:
    X = get_X(r)
    f = fx(X)
    D = Dfx(X)
    H = Hfx(X)
    # dr = -1.*(1./H)*D
    dr = -D;

    d_decent_r = r-old_r
    if d_decent_r < max_dr:
          return r;

    t = get_step_size(r,dr)
    old_r = r
    r += t*dr

    print 'r = ' + '{0:.12f}'.format(r)

def solve():
  set_coefficient_vectors()
  r = newtons_method()
  v = sn(r)
  print 'v = ' + str(v)
  return r
    

if __name__ == "__main__":
  start = time.time()
  ans = solve()
  # plot_some()
  print "*****************"
  print '{0:.12f}'.format(ans)
  stop=time.time()
  print "runtime: " + str(stop-start) + " sec."
