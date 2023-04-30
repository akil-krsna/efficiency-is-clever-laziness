import sys

from eicl import cpu_gpu, mixed
import pandas as pd

if sys.argv[0]:
    module = sys.argv[1]
try:
    submodule = sys.argv[2]
except:
    pass
root_help = """Syntax
python eicl module_name submodule_name
available modules : cpu_gpu, mixed
type python eicl module_name help for help"""
if __name__ == "__main__":
    if module:
        if module.lower() == "cpu_gpu":
            if not submodule or submodule == "help":
                print(
                    """
    Usage:
        powerbench [options]

    Options:
        help           Show this help message and exit


    Description:
        This is a command-line application for benchmarking power consumption and efficiency. 
        The application supports benchmarking of CPU and GPU. Results can be written to an output file.
        Consolidated efficiency score is printed onto stdout.

    Examples:
    #It triggers a script respective module and submodule
    python eicl.py cpu_gpu

    #Benchmark nvidia GPU 
        python eicl.py cpu_gpu pycuda
    """
                )
            if submodule.lower() == "blender":
                cpu_gpu.blender.main()
                blender_data = pd.read_csv("./measure_energy_blender.csv", sep=";")
                uj = blender_data.iloc[-1, -1]
                time = blender_data.iloc[-1, -2]
                score = uj / (time * 1920 * 1080 * 10)
                print(f"Efficiency Score : {score:.2f}")

            elif submodule.lower() == "pycuda":
                cpu_gpu.py_cuda.main()
                pycuda_data = pd.read_csv("./measure_energy_pycuda.csv", sep=";")
                uj = pycuda_data.iloc[-1, -1]
                time = pycuda_data.iloc[-1, -2]
                score = uj / (time * 4096 * 4086 * 2)
        elif module == "mixed":
            ...
        else:
            print(root_help)
    else:
        print(root_help)
