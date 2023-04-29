from blender_renderer.renderer import Renderer
import eicl.config
from pyJoules.energy_meter import measure_energy
from pyJoules.device.rapl_device import RaplPackageDomain
from pyJoules.handler.csv_handler import CSVHandler


def main():
    # Set the path to your Blender executable
    csv_handler = CSVHandler("measure_energy_blender.csv")
    blender_path = eicl.config.BLENDER_PATH
    cpu = eicl.config.CPU
    scene_file = eicl.config.SCENE_PATH
    temp_dir = "/tmp/"
    render_settings = {
        "engine": "CYCLES",
        "resolution_x": 1920,
        "resolution_y": 1080,
        "samples": 10,
    }
    renderer = Renderer(blender_path, tmp_directory=temp_dir)

    with open(scene_file, "rb") as f:
        scene_bytes = f.read()

    @measure_energy(
        domains=[RaplPackageDomain(0)],
        handler=csv_handler,
    )
    def render():
        renderer.render(scene_bytes, render_settings=render_settings)

    render()
    csv_handler.save_data()
