import sys

from eicl import cpu_gpu, mixed

module = sys.argv[1]
if sys.argv[2]:
    submodule = sys.argv[2]
root_help = """Syntax
python eicl module_name submodule_name
available modules : cpu_gpu, mixed
type python eicl module_name help for help"""
if __name__ == "__main__":
    if module.lower() == "cpu_gpu":
        if submodule =="help":
            print('''
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
   ''')
        if submodule.lower() == "blender":
            cpu_gpu.blender.main()
    elif module == "mixed":
        ...
    else:
        print(root_help)
