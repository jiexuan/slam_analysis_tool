import pymap3d as pm
import plot_3d
import glob,os,sys
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os,sys,argparse

def extract_gps(gps_folder):
    lats=[]
    lons=[]
    alts=[]
    print(gps_folder)
    for gps_file in os.listdir(gps_folder):
        gps_path = os.path.join(gps_folder,gps_file)
        lines = tuple(open(gps_path, 'r'))
        for line in lines:        
            co_ordinates=line.split(" ") 
            lats.append(float(co_ordinates[0]))
            lons.append(float(co_ordinates[1]))
            alts.append(float(co_ordinates[2]))
    return (lats,lons,alts)

def extract_gps_cordinate(lats=[],lons=[],alts=[]):    
    x_arr=[]
    y_arr=[]
    z_arr=[]
    for lat,lon,alt in zip(lats,lons,alts):
        x,y,z=pm.geodetic2ecef(lat,lon,alt)
        x_arr.append(x)
        y_arr.append(y)
        z_arr.append(z)
    return (x_arr,y_arr,z_arr)

def plot_gps_3d_arg_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-n","--plots", required = True,help = "no of plots")
    ap.add_argument("-g", "--gps", required = True,help = "kitti gps folder")
    ap.add_argument("-t", "--trajectory", default=3,help = "trajectpry file")
    ap.add_argument("-x1", "--x1", default=0,help = "x co-ordinate")
    ap.add_argument("-y1", "--y1", default=2,help = "y co-ordinate")
    ap.add_argument("-z1", "--z1", default=1,help = "z co-ordinate")

    args = vars(ap.parse_args())    
    return args

#command plot_gps.py plot_count gps_folder SemanticMapPoints.txt 0 2 1
if __name__ == '__main__':
    plot_gps_3d_arg = plot_gps_3d_arg_parser()
    #plot gps co-ordinate in 3d
    graph = plot_3d.create_3d(int(plot_gps_3d_arg['plots']))
    lats,lons,alts=extract_gps(plot_gps_3d_arg['gps'])
    gps_x_arr,gps_y_arr,gps_z_arr=extract_gps_cordinate(lats,lons,alts)
    graph(gps_x_arr,gps_z_arr,gps_y_arr)

    #plot ground truth in 3d
    if len(sys.argv) >= 6:
        x_index,y_index,z_index = (int(plot_gps_3d_arg['x1']),int(plot_gps_3d_arg['y1']),int(plot_gps_3d_arg['z1']))        
        gnd_x_arr,gnd_y_arr,gnd_z_arr=plot_3d.extract_cordinate(plot_gps_3d_arg['trajectory'],x_index,y_index,z_index )
        scale_gnd_x_arr = [x1+x2 for x1,x2 in zip(gps_x_arr,gnd_x_arr)]
        scale_gnd_y_arr = [x1+x2 for x1,x2 in zip(gps_z_arr,gnd_y_arr)]
        scale_gnd_z_arr = [x1+x2 for x1,x2 in zip(gps_z_arr,gnd_z_arr)]
        graph(scale_gnd_x_arr,scale_gnd_y_arr,scale_gnd_z_arr,'r')
    plot_3d.show()