from tetrisEnv import Tetris
import cv2


Tetris=Tetris(20,8)
i=0
Tetris.reset()
while True:
    move=3
   # k = cv2.waitKey(1)
    # if k == ord('a'): move=0
    # elif k == ord('w'): move=2
    # elif k == ord('d'): move=1
    # elif k == ord('q'): break

    i+=1
    print(i)
    a,s,d,f, g=Tetris.iteration(move)
    