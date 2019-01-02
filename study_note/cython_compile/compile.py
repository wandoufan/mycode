#! /usr/bin/env python
# -*- coding: utf-8 -*_

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import os
import sys


def find_extensions(source, extension_list=None):
    if extension_list is None:
        extension_list = []
    file_list = os.listdir(source)
    for file in file_list:
        whole_path = os.path.join(source, file)
        if os.path.isdir(whole_path):
            find_extensions(whole_path, extension_list)
        elif file.endswith('.py'):
            module_name = whole_path.strip('./')
            module_name = module_name[:-3]
            module_name = module_name.replace('/', '.')
            extension_list.append((module_name, [whole_path]))
    return extension_list


def clear_source(source, suffixs):
    file_list = os.listdir(source)
    for file in file_list:
        whole_path = os.path.join(source, file)
        if os.path.isdir(whole_path):
            clear_source(whole_path, suffixs)
        elif any(file.endswith(suffix) for suffix in suffixs):
            os.remove(whole_path)


if __name__ == '__main__':
    ext_modules = find_extensions('.')

    if sys.argv[1] == 'list_src':
        print('\n'.join('%s %s' % (ext[0], str(ext[1])) for ext in ext_modules))
    elif sys.argv[1] == 'build_ext':
        setup(
            name="main_model",
            cmdclass={'build_ext': build_ext},
            ext_modules=[Extension(name, files) for name, files in ext_modules]
        )
    elif sys.argv[1] == 'clear_compile':
        clear_source('.', ['.so', '.c', '.o'])
    elif sys.argv[1] == 'clear_src':
        clear_source('.', ['.py', '.c', '.o'])
    else:
        print('unknown function `%s`.' % sys.argv[1])

