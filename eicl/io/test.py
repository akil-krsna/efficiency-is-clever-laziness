size = 1024 * 1024  # 1MB
filename = 'iotest.txt'

with open(filename, 'w') as f:
    f.seek(size - 1)
    f.write('\0')
    