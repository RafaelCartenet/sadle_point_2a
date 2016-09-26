from sympy import *
import numpy as np


mm=0
nn=0


# -------------------------------------------------------
#
#   REQ: sympy, numpy
#
#
#



def err(fn):
    print("m:"+str(mm) + ", n:"+str(nn))
    print("Function error:")
    print(fn)


def test():
    for tmp in range(-15, 15):
        for tmp2 in range(-15, 15):
            n = float(tmp)
            m = float(2*tmp2 + 1 - n)
            mm=m
            nn=n
            m = Symbol('m')
            n = Symbol('n')
            #
            #
            #   YOUR FUNCTION GOES HERE
            #   func = 
            #
            func = cos(2*pi*m)+sin(2*pi*n-pi/2) #Moritz
            func = sin(pi*m)*sin(pi*n-pi) #Axel
            func = sin(pi*m)*cos(pi*n) #Hampus
            #
            #
            #
            #
            # -------------------------------------------

            Dn = func.diff(n)
            Dm = func.diff(m)
            
            # calc all 1d-der  
            if (Dm.subs({'n': nn, 'm': mm}).evalf()) != 0:
                err(Dm)
                print("Dm")
                return 0
            if (Dn.subs({'n': nn, 'm': mm}).evalf()) != 0:
                err(Dn)
                print("Dn")
                return 0
            # print("1st order derivative OK")
            
            Dnn = Dn.diff(n)
            Dmm = Dm.diff(m)
            Dnm = Dn.diff(m)
            Dmn = Dm.diff(n)
            
            # calc all 2d-der 
            # if (Dmm.subs({'n': nn, 'm': mm}).evalf()) != 0:
            #     err(Dmm)
            #     print("Dmm")
            #     return 0
            # if (Dnn.subs({'n': nn, 'm': mm}).evalf()) != 0:
            #     err(Dnn)
            #     print("Dnn")
            #     return 0
            # if (Dnm.subs({'n': nn, 'm': mm}).evalf()) != 0:
            #     err(Dnm)
            #     print("Dnm")
            #     return 0
            # if (Dmn.subs({'n': nn, 'm': mm}).evalf()) != 0:
            #     err(Dmn)
            #     print("Dmn")
            #     return 0
            # #print("2nd order derivative OK")
            
            # calc determinant of hessian
            hezz = (Dmm.subs({'n': nn, 'm': mm}).evalf() * Dnn.subs({'n': nn, 'm': mm}).evalf() - (Dmn.subs({'n': nn, 'm': mm}).evalf() * (Dmn.subs({'n': nn, 'm': mm}).evalf())))
            
            if hezz==0:
                err(hezz)
                print("Hezzian wrong - H=0 - inconclusive")
                return 0

            if hezz > 0:
                if (Dmm.subs({'n': nn, 'm': mm}).evalf()) > 0:
                    print("local minima")
                if (Dmm.subs({'n': nn, 'm': mm}).evalf()) < 0:
                    print("local minima")

                err(hezz)
                print("Hezzian wrong - H>0")
                return 0
    print("SADLE POINT!")
        
test()
