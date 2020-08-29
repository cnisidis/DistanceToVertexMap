import bpy

bl_info = {
    "name": "Distance To Vertex Color",
    "author" : "Constantine Nisidis",
    "descritpion": "Bake Distance from a given point (or object) as Vertex Color",
    "version":(1,0),
    "blender": (2, 80, 0),
    "location":"",
    "warning":"WIP - ",
    "support": "TESTING",
    "category" : "Tools"
}

from . operators    import DistanceVertexColor_OT_Operator
from . properties   import DistanceColorProps
from . ui           import DISTANCEMAP_PT_SETTINGS

classes = (DistanceVertexColor_OT_Operator, DISTANCEMAP_PT_SETTINGS, DistanceColorProps)
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
    register_classes()
    bpy.types.Scene.kykeon_distance = bpy.props.PointerProperty(type=DistanceColorProps)
    #bpy.types.Scene.kykeon =  bpy.props.PointerProperty(type=KykeonSettings)
    

def unregister():
    del bpy.types.Scene.kykeon_distance
    unregister_classes()



