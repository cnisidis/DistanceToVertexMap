import bpy

bl_info = {
    "name": "Distance To Vertex Color",
    "author" : "Constantine Nisidis",
    "descritpion": "PERDIX Toolkit: Bake Distance from a given point (or object) to Vertex Color Map",
    "version":(1,1),
    "blender": (2, 80, 0),
    "location":"",
    "warning":"WIP - ",
    "support": "TESTING",
    "category" : "Tools"
}

from . operators    import DistanceVertexColor_OT_Operator, DistanceToWeight_OT_Operator
from . properties   import DistanceColorProps
from . ui           import DISTANCEMAP_PT_SETTINGS

classes = (DistanceVertexColor_OT_Operator, DistanceToWeight_OT_Operator, DISTANCEMAP_PT_SETTINGS, DistanceColorProps)
register_classes, unregister_classes = bpy.utils.register_classes_factory(classes)

def register():
    register_classes()
    bpy.types.Scene.PERDIX_distance = bpy.props.PointerProperty(type=DistanceColorProps)
    #bpy.types.Scene.PERDIX_invert =bpy.props.BoolProperty(type=DistanceColorProps)
    #bpy.types.Scene.kykeon =  bpy.props.PointerProperty(type=KykeonSettings)
    

def unregister():
    del bpy.types.Scene.PERDIX_distance
    #del bpy.types.Scene.PERDIX_invert
    unregister_classes()



