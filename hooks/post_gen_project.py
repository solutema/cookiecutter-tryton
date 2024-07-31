from cookiecutter.main import cookiecutter
import datetime
import json
import os
import shutil

today = datetime.datetime.today()
date = today.date().isoformat()
year = today.year

extra_context = {
        'release_date': date,
        'year': year
        }

try:
    os.symlink('doc/index.rst', 'README.rst')
except (AttributeError, OSError):
    shutil.copyfile('doc/index.rst', 'README.rst')
