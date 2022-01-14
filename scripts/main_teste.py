#!/python3
import os
import pkgutil

os.system("echo 'teste'")

print(pkgutil.get_data('Test_Setup', 'config/config.config').decode())
