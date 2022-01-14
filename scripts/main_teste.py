#!/python3
import os
import pkgutil
import sys

file_path = os.path.join(sys.prefix, 'config.config')

print(config)

with open(config, "r") as conf:
  print(conf.read())
  


