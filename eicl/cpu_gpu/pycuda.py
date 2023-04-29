import pycuda.autoinit
import pycuda.driver as drv
import numpy as np
from pycuda.compiler import SourceModule

def perform_bench():
    # Define the matrix dimensions
    N = 4096
    M = 4096

    # Define the CUDA kernel code for matrix multiplication
    mod = SourceModule("""
        __global__ void matrix_mult(float* a, float* b, float* c, int n, int m) {
            int i = blockIdx.x * blockDim.x + threadIdx.x;
            int j = blockIdx.y * blockDim.y + threadIdx.y;

            if (i < n && j < m) {
                float sum = 0.0;
                for (int k = 0; k < n; k++) {
                    sum += a[i * n + k] * b[k * m + j];
                }
                c[i * m + j] = sum;
            }
        }
    """)

    # Get the kernel function
    matrix_mult_kernel = mod.get_function("matrix_mult")

    # Create the input matrices on the CPU
    a = np.random.rand(N, M).astype(np.float32)
    b = np.random.rand(M, N).astype(np.float32)

    # Create the output matrix on the GPU
    c_gpu = drv.mem_alloc(N * N * np.dtype(np.float32).itemsize)

    # Set the block and grid sizes for the kernel
    block_size = (32, 32, 1)
    grid_size = ((N + block_size[0] - 1) // block_size[0], (N + block_size[1] - 1) // block_size[1], 1)

    # Call the kernel function to perform matrix multiplication
    matrix_mult_kernel(drv.In(a), drv.In(b), c_gpu, np.int32(N), np.int32(M), block=block_size, grid=grid_size)

    # Copy the output matrix from the GPU to the CPU
    c = np.empty_like(a)
    drv.memcpy_dtoh(c, c_gpu)

import time 
import GPUtil

duration = 10
gpus = GPUtil.getGPUs()

shit = []

start_time = time.time()
# Print information about each GPU
while time.time() - start_time < duration: 
    
    perform_bench()
    
    for gpu in gpus:
        
#         print(time.time())
        
        GpuMemusage = gpu.memoryUsed/1024
    
        shit.append(GpuMemusage/1024)
        
        print(shit)
        
    time.sleep(1)

print(shit)

# import numpy as np
# import pyopencl as cl

# anp = np.random.rand(50000).astype(np.float32)
# bnp = np.random.rand(50000).astype(np.float32)

# ctx = cl.create_some_context()
# queue = cl.CommandQueue(ctx)

# mf = cl.mem_flags
# ag = cl.Buffer(ctx,mf.READ_ONLY|mf.COPY_HOST_PTR,hostbuf=anp)
# bg = cl.Buffer(ctx,mf.READ_ONLY|mf.COPY_HOST_PTR,hostbuf=bnp)

# prg = cl.Program(ctx, """
# __kernel void sum(
#     __global const float *a_g, __global const float *b_g, __global float *res_g)
# {
#   int gid = get_global_id(0);
#   res_g[gid] = a_g[gid] + b_g[gid];
# }
# """).build()

# resg = cl.Buffer(ctx,mf.WRITE_ONLY,anp.nbytes)
# knl = prg.sum
# knl(queue,anp.shape,None,ag,bg,resg)

# resnp = np.empty_like(anp)
# cl.enqueue_copy(queue,resnp,resg)

# print(resnp-(anp+bnp))
# print(np.linalg.norm(resnp-(anp+bnp)))
# assert np.allclose(resnp,anp+bnp)