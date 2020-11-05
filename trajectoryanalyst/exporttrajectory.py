import bpy
from __future__ import print_function

DATA = bpy.data
outputFolder= "OUTPUT.csv"

for clip in DATA.movieclips:
    width=clip.size[0]
    height=clip.size[1]
    
    for object in clip.tracking.objects:
        for track in object.tracks:
            
            file_name = outputFolder
            f = open(file_name, 'w')
            framenum = 0
            
            if framenum ==0:
                print('x,y',file=f) 
                
            while framenum < clip.frame_duration:
            
                markerAtFrame = track.markers.find_frame(framenum)
                
                if markerAtFrame:
                    coords = markerAtFrame.co.xy
                    print('{0},{1}'.format(coords[0]*width, coords[1]*height), file=f)
                    
                framenum += 1

f.close()
