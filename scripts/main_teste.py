#!/python3
import os
import pkgutil

os.system("echo 'teste'")
pt = os.path.dirname(os.path.realpath(__file__))
config = os.path.join(pt, 'config/config.config')
print(config)

with open(coonfig, "r") as conf:
  print(conf.read())
  


