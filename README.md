# DistanceToVertexMap
Blender : Bake Distance as Vertex Color or Weight Map

**TO WEIGHT MAP**

![alt text](https://github.com/cnisidis/DistanceToVertexMap/blob/master/preview_image_02.png?raw=true)

![alt text](https://github.com/cnisidis/DistanceToVertexMap/blob/master/preview_image_01.png?raw=true)

![alt text](https://github.com/cnisidis/DistanceToVertexMap/blob/master/preview_image_03.png?raw=true)

**TO VERTEX COLOR**

![alt text](https://github.com/cnisidis/DistanceToVertexMap/blob/master/preview_image.png?raw=true)

[![whatever](https://img.youtube.com/vi/B6kxMKF8gWA/0.jpg)](https://www.youtube.com/watch?v=B6kxMKF8gWA)

**CAUTION**
- After the last update the "ToVertexColor" Operator is broken (WIP)

**How it works**

- In order to work properly you must use an EMPTY as a "target" (influence) object. Thus for the order you will pick the objects doesn't matter.

- Be sure that you have selected your MESH type object and on EMPTY object

- ToVertexColor will create a vertex color map (Red Channel)

- ToWeightMap will write the distance value as per vertex weight (normalized)


**TODO**

- Calculate the mean distance from multiple points (blending)
- Add Pointer properties in UI for selecting objects interactively






