from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import glob,os,argparse

def extract_cordinate(gps_folder=r"D:\HAD\orb_slam2_world\slam_data\kitty\2011_09_30_drive_0027_sync\2011_09_30\2011_09_30_drive_0027_sync\oxts\data"):
    lats=[]
    lons=[]
    for gps_file in os.listdir(gps_folder):
        gps_path = os.path.join(gps_folder,gps_file)
        lines = tuple(open(gps_path, 'r'))
        for line in lines:        
            co_ordinates=line.split(" ") 
            lats.append(float(co_ordinates[0]))
            lons.append(float(co_ordinates[1]))
    return (lats,lons)

def drawmap(lats=[],lons=[]):
    map = Basemap(projection='merc', lat_0 = lats[0], lon_0 = lons[0],
        resolution = 'h', area_thresh = 1.5,
        llcrnrlon=lons[0]-1, llcrnrlat=lats[0]-1,
        urcrnrlon=lons[0]+1, urcrnrlat=lats[0]+1)
    
    map.drawcoastlines()
    map.drawcountries()
    map.fillcontinents(color = 'coral')
    map.drawmapboundary()
    
    x,y = map(lons[1:], lats[1:])
    map.plot(x, y, 'bo', markersize=18)
    plt.show()

def plot_gps_arg_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-g","--gps", required = True,help = "kitti gps folder")

    args = vars(ap
#command plot_gps.py gps_folder
if __name__ == '__main__':
    plot_gps_arg = plot_gps_arg_parser()
    lats,lons=extract_cordinate(plot_gps_arg['gps'])
    drawmap(lats,lons)