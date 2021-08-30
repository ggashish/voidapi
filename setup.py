
from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='voidapi',
      author='Ashish Yadav',
      author_email='ashugodhai@gmail.com',
      version='1.0.1',
      packages=['voidapi'],
      license='MIT',
      description='A simple API wrapper for voidbots.net.',
      long_description=readme,
      )