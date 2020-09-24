import numpy as np
from PIL import Image
import cv2
import pprint

colors=[(0, 0,0),
        (221 ,  51    , 68),
        (221 , 221 , 51),
        ( 51 , 221 , 71 ),
        ( 28, 221 ,163),
        (160 ,  28, 221 )]

class Show:
    def __init__(self):
        pass

    def show(self, field, a, a_color, scale):
        main=[[z for z in i] for i in field]

        H=len(main)*scale
        W=len(main[0])*scale
        for i in a:
            if(i[1]==H/scale):continue
            main[i[1]][i[0]]=a_color

        env = np.zeros((H, W, 3), dtype=np.uint8)
        for i in range(0,H):
            for z in range(W):
                env[H-1-i][z]=colors[int(main[int(i/scale)][int(z/scale)])]


        cv2.imshow('image', env)
        #cv2.waitKey(300)
       
