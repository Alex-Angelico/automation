import shutil

with open('content.txt', 'r') as f:
    f.read(content)

shutil.copy('content.txt', '/assets')
