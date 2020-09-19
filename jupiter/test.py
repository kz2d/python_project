from NN import NN
import pandas as pd
import plotly.express as px

v=NN(0.1,4,3)
df = pd.read_csv("flower.csv")

def answer(a):
    if a[0]>a[1]:
        if a[0]>a[2]:
            return 0
        if a[0]<a[2]:
            return 2
    else:
        if a[1]>a[2]:
            return 1
        if a[1]<a[2]:
            return 2

def fit(outp, right):
    c=0
    for i in range(3):
        s=right[i]-outp[i]
        c+=s**2
    return c

a=[]
a_test=[]
error=[]
error1=[]
for i in range(100):
    error.append(0)
    a.append(0)
    a_test.append(0)
    error1.append(0)
    for h in range(40):
        v.lern([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[1,0,0],a,i)
        if answer(v.neyron[-1])!=0:
            error[i]+=1
    for h in range(50,90):
        v.lern([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[0,1,0],a,i)
        if answer(v.neyron[-1])!=1:
            error[i]+=1
    for h in range(100,140):
        v.lern([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]],[0,0,1],a,i)
        if answer(v.neyron[-1])!=2:
            error[i]+=1
    # for h in range(40,50):
    #     v.Work([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]])
    #     a_test[i]+=fit(v.neyron[-1],[1,0,0])
    #     if answer(v.neyron[-1])!=0:
    #         error1[i]+=1
    # for h in range(90,100):
    #     v.Work([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]])
    #     a_test[i]+=fit(v.neyron[-1],[0,1,0])
    #     if answer(v.neyron[-1])!=1:
    #         error1[i]+=1
    # for h in range(140,150):
    #     v.Work([df.iloc[h][0],df.iloc[h][1],df.iloc[h][2],df.iloc[h][3]])
    #     a_test[i]+=fit(v.neyron[-1],[0,0,1])
    #     if answer(v.neyron[-1])!=2:
    #         error1[i]+=1
fig=px.line(a)
fig.write_html ( 'first_figure1.html' , auto_open = True )
fig1=px.line(error)
fig1.write_html ( 'first_figure1.html' , auto_open = True )