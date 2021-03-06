from math import exp
import random

class NN:
    def __init__(self,cof, inpNeuron, outpNeyron, *shadowNeyron ):#горизонт- входящие вертикаль- выходящие
        self.coficent=cof

        d=[inpNeuron,*shadowNeyron,outpNeyron]
        self.wes=[self.ArrayS(d[i]+1,d[i+1]) for i in range(len(d)-1)]
        self.errors = [[0 for j in range(d[i])] for i in range(1,len(d))]
        self.neyron=[[0 for j in range(d[i])] for i in range(len(d))]
        self.neyron_2 = [[0 for j in range ( d[i] )] for i in range ( len ( d ) )]


    def Work(self, inp):
        wes=self.wes
        c=inp
        self.neyron[0]=inp
        for i in range(len(wes)):
            d=self.neyron[i+1]
            self.calc(wes[i],c,d, self.neyron_2[i+1])
            c=d
            self.neyron[i+1]=d

    def error_find(self, wes):
        for i in range(len(self.errors)-1,0,-1):
            d=self.errors[i-1]
            self.error(wes[i], self.errors[i],self.neyron_2[i],d)
            self.errors[i-1]=d

    def bac_prop(self, wes):
        for i in range(len(wes)):
            self.Back_prop_litl(self.coficent,wes[i], self.neyron[i],self.errors[i])

    def sigmoid(self, x):
        print(x)
        return 1/(1+exp(-x))

    def calc(self, Wes, inp, outp, neyron2):
        for i in range(len(Wes)):
            outp[i]=0
            for h in range(len(Wes[0])-1):
                outp[i]+=Wes[i][h]*inp[h]
            outp[i] += Wes[i][-1]
            neyron2[i]=outp[i]
            outp[i]=self.sigmoid(outp[i])

    def error(self, Wes, RightError, ItVallue, LeftError):
        for i in range(len(Wes[0])-1):
            LeftError[i]=0
            for h in range(len(Wes)):
                LeftError[i]+=RightError[h]*Wes[h][i]
            LeftError[i]*=ItVallue[i]*(1-ItVallue[i])

    def Back_prop_litl(self, cof, Wes, vxod, ErrorItNeqron):
        for i in range(len(Wes)):
            for h in range(len(Wes[0])-1):
                Wes[i][h]+=cof*ErrorItNeqron[i]*vxod[h]
            Wes[i][-1] += cof * ErrorItNeqron[i] * 1

    def show(self):
        j = 0
        for i in self.wes:
            print ( j )
            for c in i:
                print ( c )
            j = j+1

    def ArrayS(self, int1:"вход", int2:"выход"):
        return [[random.random()-0.5 for j in range(int1)] for i in range(int2)]

    def lern(self, inp, outp, fitness:list,f:int):#f is number of list
        self.Work(inp)
        c=0
        for i in range(len(outp)):
            self.errors[-1][i]=outp[i] - self.neyron[-1][i]
            c+=self.errors[-1][i]**2
            self.errors[-1][i] *= self.neyron_2[-1][i]*(1-self.neyron_2[-1][i])
            print(self.neyron_2)
        fitness[f]+=c
        self.error_find(self.wes)
        self.bac_prop(self.wes)

# v=NN(0.1,3,2,2,2)
# a = []
# # print(v.wes)
# for i in range(100):
#     a.append(0)
#     v.lern([1,2,3],[1,0.5],a,i)
#     print(v.errors)
# fig=px.line(a)
# fig.write_html ( 'first_figure1.html' , auto_open = True )

