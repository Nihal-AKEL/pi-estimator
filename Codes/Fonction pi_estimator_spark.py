#Importation des bibliothèques nécessaires

from pyspark.sql import SparkSession
import numpy as np
from time import time
from random import random
from operator import add

#Initialisation de la SparkSession

spark=SparkSession.builder.appName('CalculatePi').getOrCreate()
sc=spark.sparkContext

#Fonction qui définit si un point est dans le cercle unitaire

def is_point_inside_unit_circle(p):
...     x, y = random(), random()
...     return 1 if x*x + y*y < 1 else 0

#Fonction qui estime pi et le temps de calcul

def pi_estimator_spark(n):
...     t=time()
...     count = sc.parallelize(range(0, n))\
...             .map(is_point_inside_unit_circle).reduce(add)
...     pi= count/n*4
...     t_cal=np.round(time()-t,2)
...     print ("Le temps de calcul est de: ", t_cal ,". Pi est éstimé à: ",pi)
...     return pi