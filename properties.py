import bpy

class DistanceColorProps(bpy.types.PropertyGroup):
    object_to_bake : bpy.props.PointerProperty(type=bpy.types.Mesh, name='To Bake')
