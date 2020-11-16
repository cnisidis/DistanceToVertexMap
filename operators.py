import bpy
from . DistanceToVertexData import DistanceToVertexColor
from . DistanceToVertexData import DistanceToWeightMap

class DistanceVertexColor_OT_Operator(bpy.types.Operator):
    bl_idname = "distance.to_color"
    bl_label = "Distance To Vertex Color"
    bl_description = "Bake Distance (from a point) as Vertex Color"
    bl_options = {'REGISTER'}


    def execute(self, context):
        scene = context.scene
        object_to_bake = bpy.context.selected_objects[0]
        from_target_object = bpy.context.selected_objects[1]
        DistanceToVertexColor(object_to_bake, from_target_object)
        self.report({'INFO'}, "Baking...")
        return {'FINISHED'}



class DistanceToWeight_OT_Operator(bpy.types.Operator):
    bl_idname = "distance.to_weight"
    bl_label = "Distance To Vertex Weight"
    bl_description = "Bake Distance (from a point) as Weight Map"
    bl_options = {'REGISTER'}


    def execute(self, context):
        scene = context.scene
        
        # if object_to_bake.type != 'MESH':
        #     print('selected object not MESH')
        # print(object_to_bake.type, from_target_object.type)
        DistanceToWeightMap()
        self.report({'INFO'}, "Baking...")
        return {'FINISHED'}