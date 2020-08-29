import bpy

class DISTANCEMAP_PT_SETTINGS(bpy.types.Panel):
    bl_label = "Distance Map"
    bl_idname = "DISTANCE_PT_Settings"
    bl_category = "KYKEON"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    

    def draw(self, context):

        layout = self.layout
        row = layout.row()
        row.label(text="Bake Distance (from Selected to Active) as Vertex Color")
        row = layout.row()
        row.operator("distance.to_color", text="ToVertexColor")
        #row.prop_search(context.scene, "object", context.scene, "objects")
        