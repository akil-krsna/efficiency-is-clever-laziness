import sys

from eicl import cpu_gpu, mixed

module = sys.argv[1]
submodule = sys.argv[2]
if __name__ == "__main__":
    if module == "cpu_gpu":
        if submodule == "blender":
            cpu_gpu.blender.main()
