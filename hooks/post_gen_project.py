import os
import shutil
from datetime import datetime

current_year = datetime.now().year

context = {{ cookiecutter }}
context["_year"] = current_year

try:
    os.symlink('doc/index.rst', 'README.rst')
except (AttributeError, OSError):
    shutil.copyfile('doc/index.rst', 'README.rst')
