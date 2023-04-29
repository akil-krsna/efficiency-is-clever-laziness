import sys

from eicl import cpu_gpu, mixed

module = sys.argv[1]
if sys.argv[2]:
    submodule = sys.argv[2]
root_help = """Syntax
python eicl module_name submodule_name
available modules : cpu_gpu, mixed, io
type python eicl module_name help for help"""
if __name__ == "__main__":
    if module.lower() == "cpu_gpu":
        if submodule == "help":
            print("""available submodules : blender""")
        if submodule.lower() == "blender":
            cpu_gpu.blender.main()
    elif module == "mixed":
        ...
    elif module == "io":
        ...
    elif module == "help":
        if submodule == "":
            print(root_help)
    else:
        print(root_help)
