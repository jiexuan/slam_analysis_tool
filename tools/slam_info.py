from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import os,sys,argparse
import unicodecsv as csv
import numpy as np
import seaborn as sns

def split_result(result):
    val,percentage_val = result.split('(')
    percentage_val = val.strip(')')
    return (val,percentage_val)

def extract_slam_info(osv_file):
    slam_info_list={}
    with open(osv_file, 'rb') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=',')
        for index,row in enumerate(csvreader):           
            if index == 2:           
                slam_info_list['total_frame'] = row[0]
                slam_info_list['total_local_key_frame'],slam_info_list['total_local_key_frame_percentage'] = split_result(row[1])
                slam_info_list['total_global_key_frame'],slam_info_list['total_global_key_frame_percentage'] = split_result(row[2])
                slam_info_list['total_local_map_point'] = row[3]
                slam_info_list['total_global_map_point'],slam_info_list['total_global_map_point_percentage'] = split_result(row[4])
            elif index == 14:
                slam_info_list['total_semantic_frame'],slam_info_list['total_semantic_frame_percentage']=split_result(row[0])
                slam_info_list['total_semantic_local_key_frame'] ,slam_info_list['total_semantic_local_key_frame_percentage']= split_result(row[1])
                slam_info_list['total_semantic_global_key_frame'] ,slam_info_list['total_semantic_global_key_frame_percentage']= split_result(row[2])
                slam_info_list['total_semantic_local_map_point'] = row[3]
                slam_info_list['total_semantic_global_map_point'],slam_info_list['total_semantic_global_map_point_percentage']= split_result(row[4])
    return slam_info_list


def draw_histpgram1(slam_info):
    plt.hist(slam_info.values(), color='orange')
    legend = ['total_frame', 'total_local_key_frame','total_global_key_frame','total_local_map_point','total_global_map_point','total_global_map_point_percentage',
            'total_semantic_frame','total_semantic_frame_percentage','total_semantic_local_key_frame','total_semantic_local_key_frame_percentage','total_semantic_global_key_frame','total_semantic_global_key_frame_percentage',
            'total_semantic_local_map_point','total_semantic_global_map_point','total_semantic_global_map_point_percentage']
    plt.xlabel("slam units")
    plt.ylabel("Frequency")
    plt.legend(legend)
    plt.xticks(range(0, 7))
    plt.yticks(range(1, 20))
    plt.title('orb-slam2 result')
    plt.show()

def get_cmap(n, name='hsv'):
    from random import randint
    colors = []

    for i in range(n):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
    return colors

def draw_histpgram(slam_info):
    frequencies = slam_info.values()
    legend1 = slam_info.keys()
    sns.set()
    plt.hist(x=frequencies, bins= 50 , color=get_cmap(17),label=legend1)
    plt.legend(legend1)
    #plt.xticks(range(0, 7))
    plt.title("histogram") 
    plt.show()
    #print(slam_info.values())
    #n, bins, patches = plt.hist(x=slam_info.values(), bins= [0,20,40,60,80,100]) , color='#0504aa',
                            #alpha=0.7)
    #legend = ['total_frame', 'total_local_key_frame','total_global_key_frame','total_local_map_point','total_global_map_point','total_global_map_point_percentage',
            #'total_semantic_frame','total_semantic_frame_percentage','total_semantic_local_key_frame','total_semantic_local_key_frame_percentage','total_semantic_global_key_frame','total_semantic_global_key_frame_percentage',
            #'total_semantic_local_map_point','total_semantic_global_map_point','total_semantic_global_map_point_percentage']
    #plt.xlabel("slam units")
    #plt.ylabel("Frequency")
    #plt.grid(axis='y', alpha=0.75)
    #plt.hist(slam_info.values(), bins=17)
    #plt.legend(legend)
    #plt.xticks(range(0, 7))
    #plt.yticks(range(1, 20))
    #plt.title('orb-slam2 result')
    #plt.show()

def slam_info_arg_parser():
    ap = argparse.ArgumentParser()
    ap.add_argument("-c","--csv", required = True,help = "orbslam2 csv file")

if __name__ == '__main__':
    slam_info_arg = slam_info_arg_parser()
    slam_info=extract_slam_info(slam_info_arg['csv'])
    draw_histpgram(slam_info)
    #plt.hist(x, bins=20)
    #plt.ylabel('No of times')
    #plt.show()
    #print(slam_info)