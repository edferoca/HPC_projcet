#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import test
import sys
import numpy as np
 

largo1=sys.argv[1]
largo2=sys.argv[2]
iteraciones=sys.argv[3]
archivo_test='Examples/{m1}x{m2}/LifeGame_{m1}x{m2}_iter{iter}.txt'.format(m1=largo1,m2=largo2,iter=iteraciones)
if int(iteraciones)<100:
    archivo_aRevisar='Life_00{iter}.txt'.format(iter=iteraciones)
elif int(iteraciones)<1000:
    archivo_aRevisar='Life_0{iter}.txt'.format(iter=iteraciones)
else:
    archivo_aRevisar='Life_{iter}.txt'.format(iter=iteraciones)


matriz_test=np.loadtxt(archivo_test)
matriz_aRevisar=np.loadtxt(archivo_aRevisar)

print(np.array_equal(matriz_test,matriz_aRevisar))

