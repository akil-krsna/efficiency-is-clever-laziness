from blender_renderer.renderer import Renderer
import eicl.config
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler

# Set the path to your Blender executable
blender_path = eicl.config.BLENDER_PATH
cpu = eicl.config.CPU
# Set the path to your Blender scene file
if cpu:
    scene_file = eicl.config.SCENE_PATH
else:
    scene_file = eicl.config.SCENE_PATH_GPU

# Initialize the renderer with the Blender executable path and a temporary directory to use
renderer = Renderer(blender_path, "/tmp")

csv_handler = CSVHandler("measure_energy.csv")

# Load the scene file
with open(scene_file, "rb") as f:
    scene_bytes = f.read()

# Create a dictionary mapping texture names to texture data

render_settings = renderer.get_render_settings(scene_bytes=scene_bytes)
# Set the render settings
# render_settings = {
#     "engine": "CYCLES",
#     "resolution_x": 1920,
#     "resolution_y": 1080,
#     "samples": 128,
# }


@measure_energy(handler=csv_handler)
# Render the image
def render():
    img_bytes = renderer.render(
        scene_bytes,
        render_settings=render_settings,
    )


# Save the image to a file
# with open("output.png", "wb") as f:
#     f.write(img_bytes)
