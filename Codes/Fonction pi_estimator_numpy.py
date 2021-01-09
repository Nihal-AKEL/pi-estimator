#Importation des bibliothèques nécessaires

import random as r
from time import time
import numpy as np

#Fonction qui estime pi

def pi_estimator_numpy(n):
	t=time()
    n_in = 0   
    for i in range(0,n):
      x = r.random()
      y = r.random()
      if (x**2 + y**2) < 1.0:
        n_in += 1
    t_cal=np.round(time()-t,2)
    pi=(float(n_in) /n) * 4
    print ("Le temps de calcul est de: ", t_cal ,". Pi est éstimé à: ",pi)
    return  pi