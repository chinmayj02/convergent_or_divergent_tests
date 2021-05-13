"""Convergence_Divergence_Tests.py, by Chinmay Joshi, 2021-01-28
   This program lets the user to test the convergence or divergence of an infinite series,
   just by taking n'th term as input.
"""

import math
import random
from sympy import *
from goto import *

n=Symbol('n')
# nth term 'an' is 'f' here
f=Function('f')(n)
g=Function('g')(n)
choice=input("To test a positive series enter '1'.\nTo test an alternating series enter '2'.\n")
if(int(choice)==1):
 f=input("Enter the n'th term: \n")
# to check nth term divergence test
 r1=limit(f,n,oo)
 print("After performing nth Term Divergence Test,r = ",float(r1))
 if(r1!=0):
# means test successful,divergent
  print("The series is Divergent\n")
 elif(r1==0):
# means test failed
  print("Test fails")
  print("Proceed to next test? [y/n]")
  if(input()=='y' or input()=='Y'):
# geometric series test
   f=simplify(f)
   f1=f
   f2=f.subs(n,n-1)
   f3=f.subs(n,n-2)
   ratio1=f2/f3
   ratio2=f1/f2
   ratio1=simplify(ratio1)
   ratio2=simplify(ratio2)
   if(ratio1==ratio2):
# means ratio is same and the series is a geometric series        
    r2=ratio1
    print("The series is an Infinite Geometric Series with ratio r = ",r2)
    if(r2<1):
# means test successful,convergent          
     print("The series is Convergent\n")
    elif(r2>=1):
# means test successful,divergent 
     print("The series is Divergent\n")
    else:
# means test failed         
     print("Test Fails")  
   else:
    pass
# d'lamberts ratio test
   f=simplify(f)
   r3=limit(f.subs(n,n+1)/f,n,oo)
   print("After performing D'Alembert's Ratio Test,r = ",r3)
   if(r3<1):
# means test successful,convergent  
    print("The series is Convergent\n")
   elif(r3>1):
# means test successful,divergent  
    print("The series is Divergent\n")
   elif(r3==1):
# means test failed,should try raabes test  
    print("Test fails")
    print("Proceed to Raabe's Test? [y/n]")
    if(input()=='y' or input()=='Y'):
# raabes test
     f=simplify(f)
     r4=limit(n*((f/f.subs(n,n+1))-1),n,oo)
     print("After performing Raabe's Ratio Test,r = ",r4)
     if(r4>1):
# means test successful,convergent  
      print("The series is Convergent\n")
     elif(r4<1):
# means test successful,divergent  
      print("The series is Divergent\n")
     elif(r4==1):
# means test failed  
      print("Test Fails")   
      print("Proceed to Cauchy's Root Test? [y/n]")
      if(input()=='y' or input()=='Y'):
       goto .end
# cauchys root test
    elif(input()=='n' or input()=='N'):
     goto .end
    label .end
    f=simplify(f)
    r5=limit(f**(1/n),n,oo)
    if(r5<1):
# means test successful,convergent 
     print("The series is Convergent\n")
    elif(r5>1):
# means test successful,divergent 
     print("The series is Divergent\n")
    else:
# means test failed  
     print("Test Fails")
     print("Proceed to next test? [y/n]")
     if(input()=='y' or input()=='Y'):
# integral test
      r6=integrate(f,(n,1,oo))
      print("The integral of nth term is ",r6)
      if(r6==oo):
# means integral is divergent  
       print("The series is divergent")
      else:
# means integral is convergent
       print("The series is convergent")
elif(int(choice)==2):
# alternating series test
 f=input("Enter the positive part of the n'th term: \n")
 f=simplify(f)
# checking condition 1 ,ie, f(n)>=f(n+1)
 flag1=0;flag2=0
 N=random.randint(1000,10000)
 g=f
 g=g.subs(n,n+1)
 if(f.subs(n,N)>=g.subs(n,N+1)):
  flag1=1
# condition 1 fulfilled
# checking condition 2 ,ie, n->oo f->0  
  if(limit(f,n,oo)==0):
   flag2=1
# condition 2 fulfilled
  else:
   print("The alternating series is divergent")
 else:
  print("The alternating series is divergent")
 if(int(flag1)==1 and int(flag2)==1):
# both conditions fulfilled,test successful,convergent
  print("The alternating series is convergent")                                                     
else:
 print("Wrong choice,try again.") 
