# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 15:26:08 2015

@author: ajaver
"""

#%run talktools
#%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

## CSS formatting
#from IPython.display import HTML
#HTML("""
#<style>
#h1 {text-align:center; color:#111133; font-size: 220%;}
#h2 {text-align:center; color:#111155; font-size: 150%;}
#h3 {text-align:center; font-size: 140%;}
#</style>
#""")

x, y = np.random.normal(0, 1, [2, 100])
c, s = 800 * np.random.random([2, 100])

fig = plt.figure()
points = plt.scatter(x, y, c=c, s=s, alpha=0.3)
plt.grid(color="lightgray");
#
#import mpld3
#mpld3.enable_notebook()
#fig