import bpy

class DISTANCEMAP_PT_SETTINGS(bpy.types.Panel):
    bl_label = "Distance Map"
    bl_idname = "DISTANCE_PT_Settings"
    bl_category = "PERDIX"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    

    def draw(self, context):

        scene = context.scene
        PERDIX_distance = scene.PERDIX_distance

        layout = self.layout
        row = layout.row()
        row.label(text="Bake Distance (from Selected to Active) as Vertex Color")
        row = layout.row()
        row.operator("distance.to_color", text="ToVertexColor")
        row = layout.row()
        row.prop(PERDIX_distance, "bool_invert")
        row = layout.row()
        row.operator("distance.to_weight", text="ToWeightMap")
        #row.prop_search(context.scene, "object", context.scene, "objects")
        