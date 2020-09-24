from showtTetris import Show
import numpy as np
import random
from pprint import pprint
import cv2

Show=Show()

class Tetris:
    def __init__(self, H, W):
        self.H=H
        self.W=W

        self.field=np.zeros([self.H,self.W])

        self.colors_len=5

        self.SHOW=True

        self.figure=[
            [3,5,4,6],
            [3,4,5,7],
            [3,5,7,6],
            [2,3,5,7],
            [2,3,4,5],
            [1,3,5,7],
            [2,4,5,7]
        ]

        self.done=False

        self.a=self.new_a()
        
        self.a_color=np.random.randint(1,self.colors_len)


    def reset(self, show=False):
        self.SHOW=show
        self.done=False
        self.field=np.zeros([self.H,self.W])
        self.a=self.new_a()
        

    def new_a(self):
        self.fig_num=self.figure[random.randint(0,len(self.figure))-1]
        return np.array([[i%2+int(self.W/2),self.H-int(i/2)] for i in self.fig_num])

    def iteration(self, move):
        b=[[*i] for i in self.a]

        if move==0 :
            '''left'''
            self.a=[[i[0]-1,i[1]] for i in self.a]
            if not self.check():self.a=b
        elif move==1 :
            '''right'''
            self.a=[[i[0]+1,i[1]] for i in self.a]
            if not self.check():self.a=b
        elif move==2 :
            '''rotate'''
            p=self.a[1]
            for i in range(4):
                self.a[i][0]=p[0]+(self.a[i][1]-p[1])
                self.a[i][1]=p[1]-(b[i][0]-p[0])
            if not self.check():self.a=b

        reward=0
        b=self.a
        self.a=[[i[0],i[1]-1] for i in self.a]
        if not self.check():
            if b[0][1]!=self.H:
                for i in range(4):
                    self.field[b[i][1],b[i][0]]=self.a_color
                self.a_color=np.random.randint(1,self.colors_len)
                self.a=self.new_a()
                if not self.check():self.done=True
                k=0
                for i in range(0,self.H):
                    count=0
                    for z in range(self.W):
                        if self.field[i][z]!=0:count+=1
                        self.field[k][z]=self.field[i][z]
                    if(count==self.W):
                        k-=1
                        reward+=1
                    k+=1
            else:
                self.done=True
        if self.SHOW:
            Show.show(self.field, self.a,self.a_color, 18)
            if self.done:
                cv2.destroyAllWindows()
        return self.field, self.fig_num, self.done, reward, self.a
        

    def check(self):
        g=0
        for i in self.a:
            if i[0]<0 or i[1]<0 or i[0]>=self.W :return False
            elif i[1]>=self.H:g+=1
            elif self.field[i[1],i[0]]:return False
        return True
        
        
