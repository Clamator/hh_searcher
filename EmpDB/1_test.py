import numpy as np
from sys import getsizeof
import pandas as pd

gl = pd.read_csv('printer2.csv')
gl_obj = gl.select_dtypes(include=['object']).copy()

dow = gl_obj[['h', 'i','j','k', 'l', 'm', 'n']]
print(dow.info(memory_usage='deep'))
#print(dow.head())

dow_cat = dow.astype('category')

#dow2 = gl_obj.c
#print(dow_cat.info(memory_usage='deep'))
#print(dow2)