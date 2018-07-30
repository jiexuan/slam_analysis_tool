from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os,sys
import gmplot

def create_3d(total_plot=1):
    plot_index = 0
    if total_plot == 1:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
    else:
        fig = plt.figure(figsize=plt.figaspect(1/total_plot))
    def update_plot3d(x_arr,y_arr,z_arr,color='b',opaque=True):
        nonlocal plot_index
        plot_index +=1
        if total_plot ==1:
            nonlocal ax
        else:
            ax = fig.add_subplot(1, 2, plot_index, projection='3d')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        ax.scatter(x_arr, y_arr, z_arr,alpha=opaque, c=color, s=30,label="coffee")
    return update_plot3d

def show():
    plt.show()

def extract_cordinate(trajectory_file,x_index,y_index,z_index):
    x_arr,y_arr,z_arr=[],[],[]
    if os.path.isfile(trajectory_file) == True:
        lines = tuple(open(trajectory_file, 'r'))
        for line in lines:        
            co_ordinates=line.split(" ") 
            x_arr.append(float(co_ordinates[x_index]))
            y_arr.append(float(co_ordinates[y_index]))
            z_arr.append(float(co_ordinates[z_index]))
    return (x_arr,y_arr,z_arr)

#command plot_gps.py plot_count KeyFrameTrajectoryKITTI.txt 3 11 7 SemanticMapPoints.txt 0 2 1
if __name__ == '__main__':
    plot3d = create_3d(int(sys.argv[1]))
    if len(sys.argv) == 2:
        x_index,y_index,z_index=(3,11,7)
    else:
        x_index,y_index,z_index = (int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
    x_arr,y_arr,z_arr=extract_cordinate(sys.argv[2],x_index,y_index,z_index)
    plot3d(x_arr,y_arr,z_arr)
    
    if len(sys.argv) > 6:
        x_index,y_index,z_index = (int(sys.argv[7]),int(sys.argv[8]),int(sys.argv[9]))
        x_arr,y_arr,z_arr=extract_cordinate(sys.argv[6],x_index,y_index,z_index)
        plot3d(x_arr,y_arr,z_arr,'r')    
    show()


