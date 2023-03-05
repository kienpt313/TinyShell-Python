import os

# Lấy các path 
paths = os.environ['PATH'].split(os.pathsep)

# In ra các path
for path in paths:
    print(path)