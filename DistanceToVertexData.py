import bpy
import mathutils
import math
import os
import time

#os.system("cls")

def distance(v1, v2):
        #d= sqrt((x2-x1)^2 + (y2-y1)^2 + (z2-z1)^2)
        return math.sqrt( 
                    math.pow( (v1[0] - v2[0]), 2 ) + 
                    math.pow( (v1[1] - v2[1]), 2 ) + 
                    math.pow( (v1[2] - v2[2]), 2 ))

def remap(value, inMin, inMax, outMin, outMax):
    #low2 + (value - low1) * (high2 - low2) / (high1 - low1)
    return outMin + (value - inMin) * (outMax - outMin) / (inMax - inMin)


def ToDictionary(keys, values):
    return dict(zip(keys, values))

    
def GetDistances(obj=None, target=None):
    
    distances=[]
    v_indices = []
    
    

    if target == None:
        try:
            target = bpy.context.selected_objects[1]
        #get controller object (named "Center") if exists
            center_obj = target #bpy.data.objects["Center"]
        #center = center_obj.location
            center = (center_obj.location[0],center_obj.location[1],center_obj.location[2])
            print(center)
        except:
            center = (0,0,0)
    else :
        center = (target.location[0],target.location[1],target.location[2])
    

    for vertex in obj.data.vertices:
        co = vertex.co
        v_index = vertex.index
        d = distance(co, center)
        v_indices.append( v_index)
        distances.append(d)
    
    return [distances, v_indices]


def DistanceToVertexColor(obj, target):
    
    time.sleep(0.2)
    print("----STARTED----")
    
   

    time.sleep(2)

    if obj.data.vertex_colors:
        vcol_layer = obj.data.vertex_colors.active
    else:
        vcol_layer = obj.data.vertex_colors.new()


    distances = []
    v_indices = []


        
    #loop through vertices
    #for poly in obj.data.polygons:
    getall = GetDistances(obj, target)
    distances = getall[0]
    v_indices = getall[1]
    

    max_d = max(distances)
    min_d = min(distances)

    

    time.sleep(0.2)
    print("----TO DICT----")

    distances_Dict = ToDictionary(v_indices, distances)
    

    '''
    for d in distances:
        normalized_d = remap(d, min_d, max_d, 1, 0)
    '''

    
    total_itterations = len(obj.data.polygons)

    time.sleep(0.2)
    
    toVertexColor = False
    if toVertexColor :
        print("----TO COLOR----")
        for i, poly in enumerate(obj.data.polygons):
            for loop_index in poly.loop_indices:
                loop_vert_index = obj.data.loops[loop_index].vertex_index
                
                d= remap(distances_Dict[loop_vert_index], min_d, max_d, 1, 0)
                
                #if v_index == loop_vert_index:
                vcol_layer.data[loop_index].color = (d, 0,0, 0)
                
                print(d,"\t", vcol_layer.data[loop_index].color[0:4])
                print( "\n", i/total_itterations*100, "%\n")
    print("----FINISHED----")
            

def filter_selected(objects, filter_type=['MESH']):
    for obj in objects:
        if obj.type in filter_type:
            print('Found:', obj,'  --->  ', obj.type)
            return obj
        
        

def DistanceToWeightMap():
    print('SELECTED OBJECTS: ',bpy.context.selected_objects)
    obj = filter_selected(bpy.context.selected_objects, ['MESH'])
    target = filter_selected(bpy.context.selected_objects, ['EMPTY'])
    
    
    getall = GetDistances(obj, target)
    distances = getall[0]
    
    if bpy.context.scene.PERDIX_distance.bool_invert:
        max_d = min(distances)
        min_d = max(distances)
    else:
        max_d = max(distances)
        min_d = min(distances)

    
        
    print("----TO WEIGHT MAP-----")
    totalVertices = len(obj.data.vertices)

    for i, vertex in enumerate(obj.data.vertices):
        vertex.groups[0].weight = remap(distances[i], min_d, max_d, 1, 0)
        print( "\n", (i/totalVertices)*100, "%\n")
    print("----FINISHED----")

 