import {library_name}
import os

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = [r for r in map(str.strip, open('requirements.txt').readlines())]

def split_path(path, result=None):
  result = result or []
  head, tail = os.path.split(path)

  if head == '':
    return [tail] + result
  elif head == path:
    return result
  else:
    return split_path(head, [tail] + result)

def get_packages():
  packages = []
  root_dir = os.path.dirname(__file__)
  if root_dir != '':
    os.chdir(root_dir)

  for dirpath, dirnames, filenames in os.walk('snake_skin'):
    for i, dirname in enumerate(dirnames):
      if dirname.startswith('.') or dirname == '__pycache__':
        del dirnames[i]
      if '__init__.py' in filenames:
        packages.append('.'.join(split_path(dirpath)))

  return packages

setup(
  name = {library_name},
  version = {library_name}.__version__,
  url = 'LIBRARY_URL',
  author = 'AUTHOR_NAME',
  author_email = 'AUTHOR_EMAIL',
  description = 'SHORT DESCRIPTION HERE',
  packages = get_packages(),
  install_requires = requirements,
  classifiers = [
    'Programming Language :: Python',    
  ]
)
