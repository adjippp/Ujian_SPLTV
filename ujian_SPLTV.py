import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

#x - 2y + z = 6
#3x +  y - 2z =  4
#7x - 6y -  z = 10
def main_start():
    p = np.array([[1,-2,1],[3,1,-2],[7,-6,-1]])
    q = np.array([6,4,10])
    hasil = np.linalg.solve(p,q)
    print('Nilai x:', round(hasil[0]))
    print('Nilai y:', round(hasil[1]))
    print('Nilai z:', round(hasil[2]))
    createPlot()

def createPlot():
    plt.figure('Ujian SPLTV',figsize=(15,5))
    #x -2y +z = 6
    custom=plt.subplot(131,projection='3d')
    x1=np.array([6,0,0])
    y1=np.array([0,-3,0])
    z1=np.array([0,0,6])
    custom.plot_trisurf(x1,y1,z1,color='red',alpha=0.5)
    custom.scatter(x1,y1,z1,color='blue')
    custom.text2D(0.05, 0.95, "x -2y +z = 6", transform=custom.transAxes)
    custom.set_xlabel('Nilai X')
    custom.set_ylabel('Nilai Y')
    custom.set_zlabel('Nilai Z')

    #3x + y - 2z = 4
    custom2=plt.subplot(132,projection='3d')
    x2=np.array([4/3,0,0])
    y2=np.array([0,4,0])
    z2=np.array([0,0,4/-2])
    custom2.plot_trisurf(x2,y2,z2,color='yellow',alpha=0.5)
    custom2.scatter(x2,y2,z2,color='red')
    custom2.text2D(0.05, 0.95, "3x + y - 2z = 4", transform=custom2.transAxes)
    custom2.set_xlabel('Nilai X')
    custom2.set_ylabel('Nilai Y')
    custom2.set_zlabel('Nilai Z')

    #7x - 6y -z = 10
    custom3=plt.subplot(133,projection='3d')
    x3=np.array([10/7,0,0])
    y3=np.array([0,10/-6,0])
    z3=np.array([0,0,-10])
    custom3.plot_trisurf(x3,y3,z3,color='blue',alpha=0.5)
    custom3.scatter(x3,y3,z3,color='green')
    custom3.text2D(0.05, 0.95, "7x - 6y -z = 10", transform=custom3.transAxes)
    custom3.set_xlabel('Nilai X')
    custom3.set_ylabel('Nilai Y')
    custom3.set_zlabel('Nilai Z')
    plt.show()
if __name__ == "__main__":  
    main_start()