import numpy as np
from sys import getsizeof
import pandas as pd

gl = pd.read_csv('printer2.csv')
print(gl.info(memory_usage='deep'))
gl_obj = gl.select_dtypes(include=['object']).copy()

dow = gl_obj['h']
print(dow.head())

dow_cat = dow.astype('category')
print(dow_cat.info(memory_usage='deep'))

dow2 = gl_obj.a
print(dow2)