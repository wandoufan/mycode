from distutils.core import setup
from Cython.Build import cythonize
setup(name='discover new word',
      ext_modules=cythonize("wordseg.pyx"))
