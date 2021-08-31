from setuptools import setup

with open('README.md') as f:
    readme = f.read()

setup(name='voidapi',
      author='Ashish Yadav',
      author_email='ashugodhai@gmail.com',
      version='1.0.1',
      packages=['voidapi'],
      license='MIT',
      url="https://github.com/ggashish/voidapi",
      keywords = ["void", "voidbots.net"],
      install_requires = ["aiohttp", "discord.py", "python-dateutil"],
      description='A simple API wrapper for voidbots.net.',
      long_description=readme,
      long_description_content_type='text/markdown',
      classifiers=[
    'Development Status :: 5 - Production/Stable',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ])