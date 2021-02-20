import plotly.graph_objects as go
import plotly as py
import math
import sys

from numpy import arange,array,ones
from scipy import stats
import numpy as np

x=[.005, .015, .025, .035, .045, .055, .065, .075]
y=[8.410, 6.360, 5.010, 4.120, 3.433, 2.863, 2.383, 1.939]

coeffs = np.polyfit(np.log(x), y, 1)


#x=[.005, .015, .025, .035, .045, .055, .065, .075, .085, .095]
#y=[1.942, 2.848, 3.708, 4.55, 5.45, 6.28, 7.08, 7.94, 8.83, 9.68]
#slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
#print(slope)
#print()
#print(intercept)
#print()
#print(r_value**2)

#line = slope*array(x)+intercept

line2 = -2.4192*array(np.log(x))+-4.11149


correlation_matrix = np.corrcoef(x, line2)
correlation_xy = correlation_matrix[0,1]
r_squared = correlation_xy**2

print(r_squared)

def yerror(y):
    return [i*.008 + .001 for i in y]
    
ybar=[1.942, 2.848, 3.708, 4.55, 5.45, 6.28, 7.08, 7.94, 8.83, 9.68]
yerror=yerror(ybar)
    

y=[8.410, 6.360, 5.010, 4.120, 3.433, 2.863, 2.383, 1.939]

layout = go.Layout(
    title = "Relationship Between Electric Potential and the Distance from Ground Connection",
    xaxis = dict(
        title = "Distance (m)",
        showgrid=True,
        gridcolor = '#bdbdbd',
        linecolor = '#636363'
    ),
    yaxis = dict(
        title = "Electric Potential (V)",
        showgrid=True,
        gridcolor = '#bdbdbd',
        linecolor = '#636363'
    ),
       font=dict(
        family="Courier New, monospace",
        size=18,
    )
)

layout2 = go.Layout(
    title = "Relationship Between Electric Potential and the Distance from Positive Connection",
    xaxis = dict(
        title = "Distance (m)",
        showgrid=True,
        gridcolor = '#bdbdbd',
        linecolor = '#636363'
    ),
    yaxis = dict(
        title = "Electric Potential (V)",
        showgrid=True,
        gridcolor = '#bdbdbd',
        linecolor = '#636363'
    ),
       font=dict(
        family="Courier New, monospace",
        size=18,
    )
)

#layout2 = go.Layout(
#    title = "Ln(Distance) vs Ln(Corrected Radiation)",
#    xaxis = dict(
#        title = "Ln(Distance)",
#    ),
#    yaxis = dict(
#        title = "Ln(Corrected Radiation)",
#    ),
#       font=dict(
#        family="Courier New, monospace",
#        size=18,
#    )
#)

Parallel = go.Scatter(
        x=[.005, .015, .025, .035, .045, .055, .065, .075, .085, .095],
        y=[1.942, 2.848, 3.708, 4.55, 5.45, 6.28, 7.08, 7.94, 8.83, 9.68],
        mode='markers',
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=yerror,
            visible=True),

        error_x=dict(
            type='data', # value of error bar given in data coordinates
            array=[.0005] * 10,
            visible=True)
        )
   
Ring = go.Scatter(
        x=[.005, .015, .025, .035, .045, .055, .065, .075],
        y=[8.410, 6.360, 5.010, 4.120, 3.433, 2.863, 2.383, 1.939],
        mode='markers',
        error_y=dict(
            type='data', # value of error bar given in data coordinates
            array=yerror[:7],
            visible=True),

        error_x=dict(
            type='data', # value of error bar given in data coordinates
            array=[.0005] * 10,
            visible=True)
        )
#Ln = go.Scatter(
#        x=lnx,
#        y=lny,
#        mode='markers',
#        name='data points',
#        error_y=dict(
#            type='data', # value of error bar given in data coordinates
#            array=lnyError,
#            visible=True),
#
#        error_x=dict(
#            type='data', # value of error bar given in data coordinates
#            array=lnxError,
#            visible=True)
#        )
#
#line = go.Scatter(
#                  x=x,
#                  y=line,
#                  mode='lines',
#                  marker=go.Marker(color='rgb(31, 119, 180)'),
#                  name='Linear Regression'
#                  )
line2 = go.Scatter(
                  x=x,
                  y=line2,
                  mode='lines',
                  marker=go.Marker(color='rgb(31, 119, 180)'),
                  name='Linear Regression'
                  )

#data1 = [Parallel, line]
#fig1 = go.Figure(data=data1,layout=layout)

data2 = [Ring, line2]
fig2 = go.Figure(data=data2,layout=layout2)

#py.offline.plot(fig1, filename='Parallel')
py.offline.plot(fig2, filename='Ring')
