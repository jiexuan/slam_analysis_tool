from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os,sys,argparse
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

def plot3d_arg_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n","--plots", required = True,help = "no of plots")
    ap.add_argument("-t1", "--trajectory1", required = True,help = "trajectory file path")
    ap.add_argument("-x1", "--x1", default=3,help = "x co-ordinate")
    ap.add_argument("-y1", "--y1", default=11,help ="y co-ordinate")
    ap.add_argument("-z1", "--z1", default=7,help = "z co-ordinate")
    ap.add_argument("-t2", "--trajectory2", required = False,help = "trajectory file path")
    ap.add_argument("-x2", "--x2", default=0,help = "x co-ordinate")
    ap.add_argument("-y2", "--y2", default=2,help = "y co-ordinate")
    ap.add_argument("-z2", "--z2", default=1,help = "z co-ordinate")

    args = vars(ap.parse_args())    
    return args

#command plot_gps.py plot_count KeyFrameTrajectoryKITTI.txt 3 11 7 SemanticMapPoints.txt 0 2 1
if __name__ == '__main__':
    plot3d_arg = plot3d_arg_parser()
    plot3d = create_3d(int(plot3d_arg['plots']))
    if len(sys.argv) == 2:
        x_index,y_index,z_index=(3,11,7)
    else:
        x_index,y_index,z_index = (int(plot3d_arg['x1']),int(plot3d_arg['y1']),int(plot3d_arg['z1']))
    x_arr,y_arr,z_arr=extract_cordinate(plot3d_arg['trajectory1'],x_index,y_index,z_index)
    plot3d(x_arr,y_arr,z_arr)
    
    if len(sys.argv) > 6:
        x_index,y_index,z_index = (int(plot3d_arg['x2']),int(plot3d_arg['y2']),int(plot3d_arg['z2']))
        x_arr,y_arr,z_arr=extract_cordinate(plot3d_arg['trajectory2'],x_index,y_index,z_index)
        plot3d(x_arr,y_arr,z_arr,'r')    
    show()


