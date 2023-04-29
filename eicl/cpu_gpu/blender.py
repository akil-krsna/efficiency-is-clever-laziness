from blender_renderer.renderer import Renderer
import eicl.config
from pyJoules.energy_meter import measure_energy
from pyJoules.handler.csv_handler import CSVHandler


def main():
    # Set the path to your Blender executable
    csv_handler = CSVHandler("measure_energy_blender.csv")
    blender_path = eicl.config.BLENDER_PATH
    cpu = eicl.config.CPU
    scene_file = eicl.config.SCENE_PATH
    # # Set the path to your Blender scene file
    # if cpu:
    #     scene_file = eicl.config.SCENE_PATH
    #     # Set the render settings
    # else:
    #     scene_file = eicl.config.SCENE_PATH_GPU
    temp_dir = "/tmp/"
    render_settings = {
        "engine": "CYCLES",
        "resolution_x": 960,
        "resolution_y": 540,
        "samples": 1,
    }
    # Initialize the renderer with the Blender executable path and a temporary directory to use
    renderer = Renderer(blender_path, tmp_directory=temp_dir)

    # Load the scene file
    with open(scene_file, "rb") as f:
        scene_bytes = f.read()

    # Create a dictionary mapping texture names to texture data

    # render_settings = renderer.get_render_settings(scene_bytes=scene_bytes)

    # Render the image
    @measure_energy(handler=csv_handler)
    def render():
        renderer.render(scene_bytes, render_settings=render_settings)

    render()
    csv_handler.save_data()


# Save the image to a file
# with open("output.png", "wb") as f:
#     f.write(img_bytes)
