import bpy
from . DistanceToVertexColor import Distance

class DistanceVertexColor_OT_Operator(bpy.types.Operator):
    bl_idname = "distance.to_color"
    bl_label = "Distance To Vertex Color"
    bl_description = "Bake Distance (from a point) as Vertex Color"
    bl_options = {'REGISTER'}


    def execute(self, context):
        scene = context.scene
        object_to_bake = bpy.context.selected_objects[0]
        from_target_object = bpy.context.selected_objects[1]
        Distance(object_to_bake, from_target_object)
        self.report({'INFO'}, "Baking...")
        return {'FINISHED'}
