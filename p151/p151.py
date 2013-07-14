import numpy as np
import itertools as iter


def cut_at_index(p,i,prb):
    pr = (float(p[i])/sum(p))*prb
    y = list(p)
    y[i] -=1
    for j in range(i+1,5):
        y[j] += 1    
    return ((y[0],y[1],y[2],y[3],y[4]),pr)


def main():
   #index 5 is a running probability of that combination
   P = {(0,1,1,1,1):1}
   Pr = [0]
   # for k in range(0,14):
   for k in range(2,2+15):
       # print "***********************"
       #compute probabilities given each previous possible letter drawn
       P_next = []
       X = []
       prb = 0
       P_next_cum = {}
       for i in range(0,5):
           for p in P:
               if i == 0:
                   # print (p,P[p],( float(p[4])/sum(p) )*P[p])
                   prb += ( float(p[4])/sum(p) )*P[p]
               if p[i] > 0:
                   (pn,pr) = cut_at_index(p,i,P[p])
                   if pn in P_next_cum:
                       P_next_cum[pn] += pr
                   else:
                       P_next_cum[pn] =  pr

       Pr.append(prb)
       P = P_next_cum

   Pr = Pr[1:len(Pr)-1]
   PPx = []
   for k in range(1,16):
       It = iter.combinations(Pr,k)
       R = 0 
       for it in It:
           Px = 1
           for p in Pr:
               if p in it:                  
                   Px *= p
               else:
                   Px *= (1.0-p)          
           R += Px
       PPx.append(R*k)
   print np.sum(PPx)
   return 1
                   


if __name__ == "__main__":
    result  = main()
    print "###################"
    print result

