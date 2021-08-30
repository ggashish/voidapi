
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='voidbots.py',
      author='Ashish Yadav',
      author_email='ashugodhai@gmail.com',
      version='1.0.0',
      packages=['voidbots.py'],
      license='MIT',
      description='A simple API wrapper for voidbots.net.',
      long_description=readme,
      )