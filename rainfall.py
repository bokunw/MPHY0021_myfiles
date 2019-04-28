# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:28:55 2019

@author: Admin
"""
import numpy as np
import json
from matplotlib import pyplot as plt




data = np.genfromtxt('python_language_1_data.csv', delimiter=',',  skip_header=1,
                         names=['year','day','rainfall',
                         ],
                         dtype=[int, int, float])


prev_year = data["year"][0]
data_dict = {}
data_dict[prev_year] = [data["rainfall"][0]]
for i in range(1, len(data["rainfall"])):
    if data["year"][i] == prev_year:
        data_dict[prev_year].append(data["rainfall"][i])
    else:
        prev_year = data["year"][i]
        data_dict[prev_year] = [data["rainfall"][i]]

data_dict = {int(key):value for key, value in data_dict.items()}

jsonstr = json.dumps(data_dict, indent=4)

with open('json.json', 'w') as target:
    target.write(jsonstr)
    
    
def plot_daily(filename, year, line_color = "b"):
    with open(filename,'r') as source:
        data_str = source.read()
        data_dict = json.loads(data_str)
        plot1, ax = plt.subplots()
        ax.plot(data_dict[year], line_color)
        plot1.savefig('graph_daily.png')
        
        
plot_daily('json.json', "1998", line_color = "b")

def plot_annual(filename, year1, year2):
    with open(filename,'r') as source:
        data_str = source.read()
        data_dict = json.loads(data_str)
        plot2, ax2 = plt.subplots()
        ax2.plot(np.arange(int(year1), int(year2)+1, 1), [np.mean(data_dict[str(i)]) for i in np.arange(int(year1), int(year2)+1, 1)], "b")
        plot2.savefig('graph_daily.png')
        print([np.mean(data_dict[str(i)]) for i in np.arange(int(year1), int(year2), 1)])

plot_annual('json.json', "1988", "2000")

def correction(value):
    return value*1.2**np.sqrt(2)
    
def apply_for(filename, year, func):
     with open(filename,'r') as source:
        data_str = source.read()
        data_dict = json.loads(data_str)
        result = []
        for i in data_dict[year]:
            result.append(func(i))
        
        return result

def apply_comp(filename, year, func):
     with open(filename,'r') as source:
        data_str = source.read()
        data_dict = json.loads(data_str)
        return [func(i) for i in data_dict[year]]


a = apply_for('json.json', "1999", correction) 
b = apply_comp('json.json', "1999", correction)

















    
    
    
    
    
    
    