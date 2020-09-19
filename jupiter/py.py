from main import NN
import plotly.express as px
import pandas as pd
import numpy as np

df=pd.read_csv('flower.csv')
v=NN(0.1,4,3,6)
fit=[]
fit_test=[]
error=[]
error_test=[]
for i in range(500):
    fit.append(0)
    fit_test.append(0)
    error.append(0)
    error_test.append(0)
    for h in range(40):
        v.train([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[1,0,0])
        c=v.errors*v.errors
        fit[i]+=c.sum()
        if np.argmax(v.outp)!=0:
            error[i]+=1
    for h in range(50,90):
        v.train([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[0,1,0])
        c = v.errors * v.errors
        fit[i] += c.sum()
        if np.argmax(v.outp)!=1:
            error[i]+=1
    for h in range(100,140):
        v.train([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[0,0,1])
        c = v.errors * v.errors
        fit[i] += c.sum()
        if np.argmax(v.outp)!=2:
            error[i]+=1
    for h in range ( 40 , 50 ):
        v.Work ( [df.iloc[h][0] , df.iloc[h][1] , df.iloc[h][2] , df.iloc[h][3]] )
        c = np.array([1,0,0])-v.outp
        c=c*c
        fit_test[i] += c.sum ()
        if np.argmax ( v.outp ) != 0:
            error_test[i] += 1
    for h in range ( 90 , 100 ):
        v.Work ( [df.iloc[h][0] , df.iloc[h][1] , df.iloc[h][2] , df.iloc[h][3]] )
        c = np.array([0,1,0])-v.outp
        c=c*c
        fit_test[i] += c.sum ()
        if np.argmax ( v.outp ) != 1:
            error_test[i] += 1
    for h in range ( 140 , 150 ):
        v.Work ( [df.iloc[h][0] , df.iloc[h][1] , df.iloc[h][2] , df.iloc[h][3]] )
        c = np.array([0,0,1])-v.outp
        c=c*c
        fit_test[i] += c.sum ()
        if np.argmax ( v.outp ) != 2:
            error_test[i] += 1
fig=px.line(fit)
fig.write_html('first_figure.html' , auto_open = True )
fig=px.line(error)
fig.write_html('first_figure1.html' , auto_open = True )
fig=px.line(fit_test)
fig.write_html('first_figure.html' , auto_open = True )
fig=px.line(error_test)
fig.write_html('first_figure1.html' , auto_open = True )