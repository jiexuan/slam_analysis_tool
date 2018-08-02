from gmplot import gmplot
import glob,os,sys,argparse

def extract_cordinate(gps_folder):
    lats,lons=[],[]
    for gps_file in os.listdir(gps_folder):
        gps_path = os.path.join(gps_folder,gps_file)
        lines = tuple(open(gps_path, 'r'))
        for line in lines:        
            co_ordinates=line.split(" ") 
            lats.append(float(co_ordinates[0]))
            lons.append(float(co_ordinates[1]))
    return (lats,lons)

def draw_polygon_map(lats,lons):
    # Place map
    #gmplot.GoogleMapPlotter(start lat, start long, zoom)
    gmap = gmplot.GoogleMapPlotter(lats[0], lons[0], 17)
    # Polygon
    gmap.plot(lats, lons, 'cornflowerblue', edge_width=5)
    # Draw
    gmap.draw("my_polygon_map.html")

def draw_scatter_map(lats,lons):
    # Place map
    #gmplot.GoogleMapPlotter(start lat, start long, zoom)
    gmap = gmplot.GoogleMapPlotter(lats[0], lons[0], 17)
    # scatter
    gmap.scatter(lats, lons, '#3B0B39', size=3, marker=False)
    # Draw
    gmap.draw("my_scatter_map.html")

def draw_marker_map(lats,lons):
    # Place map
    #gmplot.GoogleMapPlotter(start lat, start long, zoom)
    gmap = gmplot.GoogleMapPlotter(lats[0], lons[0], 19)
    # Marker
    gmap.marker(lats[15], lons[15], 'cornflowerblue')
    # Draw
    gmap.draw("my_marker_map.html")

def plot_google_map_arg_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-g","--gps", required = True,help = "kitti gps folder")

    args = vars(ap.parse_args())    
    return args

if __name__ == '__main__':
    plot_google_map_ar = plot_google_map_arg_parser()
    lats,lons=extract_cordinate(plot_google_map_ar['gps'])
    draw_polygon_map(lats,lons)
    draw_scatter_map(lats,lons)
    draw_marker_map(lats,lons)