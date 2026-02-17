nbl_info = {
    "name": "Task 2 Mesh Tools",
    "author": "Your Name",
    "version": (1, 1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > Task2",
    "description": "Create grids, delete objects and merge meshes sharing a face",
    "category": "Object",
}

import bpy
import math
from mathutils import Vector

# UI PANEL

class TASK2_PT_MainPanel(bpy.types.Panel):
    bl_label = "Task 2 Panel"
    bl_idname = "TASK2_PT_main_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Task2'

    def draw(self, context):
        layout = self.layout

        layout.label(text="Task 2 Controls")

        layout.prop(context.scene, "task2_number")

        layout.operator("task2.print_number")
        layout.operator("task2.add_cube")
        layout.operator("task2.create_grid")
        layout.operator("task2.delete_selected")
        layout.operator("task2.merge_selected")


# OPERATORS

class TASK2_OT_PrintNumber(bpy.types.Operator):
    bl_idname = "task2.print_number"
    bl_label = "Print Number"
    bl_options = {'UNDO'}

    def execute(self, context):
        print("Number entered:", context.scene.task2_number)
        return {'FINISHED'}


class TASK2_OT_AddCube(bpy.types.Operator):
    bl_idname = "task2.add_cube"
    bl_label = "Add One Cube"
    bl_options = {'UNDO'}

    def execute(self, context):
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}


class TASK2_OT_CreateGrid(bpy.types.Operator):
    bl_idname = "task2.create_grid"
    bl_label = "Create Cube Grid"
    bl_options = {'UNDO'}

    def execute(self, context):

        n = context.scene.task2_number

        if n > 20:
            self.report({'ERROR'}, "The number is out of range")
            return {'CANCELLED'}

        cols = math.ceil(math.sqrt(n))
        rows = math.ceil(n / cols)

        spacing = 2.0
        count = 0

        for r in range(rows):
            for c in range(cols):

                if count >= n:
                    break

                bpy.ops.mesh.primitive_cube_add(
                    location=(c * spacing, r * spacing, 0)
                )

                count += 1

        return {'FINISHED'}


class TASK2_OT_DeleteSelected(bpy.types.Operator):
    bl_idname = "task2.delete_selected"
    bl_label = "Delete Selected"
    bl_options = {'UNDO'}

    def execute(self, context):

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        if not context.selected_objects:
            self.report({'WARNING'}, "No objects selected")
            return {'CANCELLED'}

        bpy.ops.object.delete()

        return {'FINISHED'}


class TASK2_OT_MergeSelected(bpy.types.Operator):
    bl_idname = "task2.merge_selected"
    bl_label = "Merge Selected Meshes"
    bl_options = {'UNDO'}

    def execute(self, context):

        selected = context.selected_objects

        if len(selected) < 2:
            self.report({'ERROR'}, "Select at least two meshes")
            return {'CANCELLED'}

        for obj in selected:
            if obj.type != 'MESH':
                self.report({'ERROR'}, "All selected objects must be meshes")
                return {'CANCELLED'}

        connected = set()

        for i in range(len(selected)):
            for j in range(i + 1, len(selected)):
                if share_face(selected[i], selected[j]):
                    connected.add(selected[i])
                    connected.add(selected[j])

        if len(connected) < 2:
            self.report({'ERROR'}, "No meshes share faces")
            return {'CANCELLED'}

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        bpy.ops.object.select_all(action='DESELECT')

        for obj in connected:
            obj.select_set(True)

        context.view_layer.objects.active = list(connected)[0]

        bpy.ops.object.join()

        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')

        try:
            bpy.ops.mesh.merge_by_distance()
        except:
            bpy.ops.mesh.remove_doubles()

        bpy.ops.mesh.normals_make_consistent(inside=False)

        bpy.ops.object.mode_set(mode='OBJECT')

        return {'FINISHED'}


# HELPER FUNCTIONS

def get_world_bbox(obj):
    mat = obj.matrix_world
    return [mat @ Vector(corner) for corner in obj.bound_box]


def share_face(obj1, obj2, tol=1e-5):

    bb1 = get_world_bbox(obj1)
    bb2 = get_world_bbox(obj2)

    min1 = Vector((min(v.x for v in bb1),
                   min(v.y for v in bb1),
                   min(v.z for v in bb1)))

    max1 = Vector((max(v.x for v in bb1),
                   max(v.y for v in bb1),
                   max(v.z for v in bb1)))

    min2 = Vector((min(v.x for v in bb2),
                   min(v.y for v in bb2),
                   min(v.z for v in bb2)))

    max2 = Vector((max(v.x for v in bb2),
                   max(v.y for v in bb2),
                   max(v.z for v in bb2)))

    touch_x = abs(max1.x - min2.x) < tol or abs(max2.x - min1.x) < tol
    overlap_y = min(max1.y, max2.y) - max(min1.y, min2.y) > tol
    overlap_z = min(max1.z, max2.z) - max(min1.z, min2.z) > tol

    touch_y = abs(max1.y - min2.y) < tol or abs(max2.y - min1.y) < tol
    overlap_x = min(max1.x, max2.x) - max(min1.x, min2.x) > tol

    touch_z = abs(max1.z - min2.z) < tol or abs(max2.z - min1.z) < tol

    return (
        (touch_x and overlap_y and overlap_z) or
        (touch_y and overlap_x and overlap_z) or
        (touch_z and overlap_x and overlap_y)
    )

# REGISTER
classes = (
    TASK2_PT_MainPanel,
    TASK2_OT_PrintNumber,
    TASK2_OT_AddCube,
    TASK2_OT_CreateGrid,
    TASK2_OT_DeleteSelected,
    TASK2_OT_MergeSelected,
)


def register():

    bpy.types.Scene.task2_number = bpy.props.IntProperty(
        name="N",
        description="Enter a number less than 20",
        default=1,
        min=1
    )

    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.task2_number


if __name__ == "__main__":
    register()
