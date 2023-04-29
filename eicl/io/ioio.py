from cbtool import Fio


# Create a Fio instance
fio = Fio()

# Define the test parameters
filename = 'iotest.bin'
filesize = '1M'
blocksize = '4k'
iodepth = 32
numjobs = 1
ioengine = 'sync'
rw = 'write'

# Run the test
result = fio.run(filename=filename, filesize=filesize, blocksize=blocksize,
                  iodepth=iodepth, numjobs=numjobs, ioengine=ioengine, rw=rw)

# Print the test results
print('Test results:')
print('---------------')
print('Filename:', result['filename'])
print('Filesize:', result['filesize'])
print('Blocksize:', result['blocksize'])
print('I/O depth:', result['iodepth'])
print('Num jobs:', result['numjobs'])
print('I/O engine:', result['ioengine'])
print('Read/write:', result['rw'])
print('Bandwidth (MB/s):', result['bw'])
print('IOPS:', result['iops'])
print('Latency (usec):')
print('  Min:', result['latency']['min'])
print('  Max:', result['latency']['max'])
print('  Mean:', result['latency']['mean'])
