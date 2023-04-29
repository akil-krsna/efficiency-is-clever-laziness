from blender_renderer.renderer import Renderer

# Set the path to your Blender executable
blender_path = "/path/to/blender"

# Set the path to your Blender scene file
scene_file = "/path/to/scene.blend"

# Set the path to your texture file
texture_file = "/path/to/texture.png"

# Initialize the renderer with the Blender executable path and a temporary directory to use
renderer = Renderer(blender_path, "/tmp")

# Load the scene file
with open(scene_file, 'rb') as f:
    scene_bytes = f.read()

# Get the texture names from the scene file
texture_names = renderer.get_texture_names(scene_bytes)

# Load the texture file
with open(texture_file, 'rb') as f:
    texture_bytes = f.read()

# Create a dictionary mapping texture names to texture data
texture_files_map = {
    texture_names[0]: texture_bytes,
}

# Set the render settings
render_settings = {
    "engine": "CYCLES",
    "resolution_x": 800,
    "resolution_y": 600,
    "samples": 128,
}

# Render the image
img_bytes = renderer.render(
    scene_bytes,
    textures=texture_files_map,
    render_settings=render_settings,
)

# Save the image to a file
with open("output.png", "wb") as f:
    f.write(img_bytes)
