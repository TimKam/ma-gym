from os import path

import setuptools
from setuptools import setup

setup(name='ma_gym',
      version='0.0.8',
      description='A collection of multi agent environments based on OpenAI gym.',
      long_description_content_type='text/markdown',
      long_description=open(path.join(path.abspath(path.dirname(__file__)), 'README.md'), encoding='utf-8').read(),
      url='https://github.com/koulanurag/ma-gym',
      author='Anurag Koul',
      author_email='koulanurag@gmail.com',
      license='MIT License',
      packages=setuptools.find_packages(),
      install_requires=[
          'scipy>=1.3.0',
          'numpy>=1.16.4',
          'pyglet>=1.4.0',
          'cloudpickle>=1.2.0,<1.7.0',
          'gym==0.19.0',
          'pillow>=7.2.0',
          'six>=1.16.0'
      ],
      python_requires='>=3.6',
      classifiers=[
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      )
