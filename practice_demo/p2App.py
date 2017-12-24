import sys
from cx_Freeze import setup, Executable

build_exe_options = {"optimize" : 2,
                     "include_files" : ["poker.py"]}

base = None

if sys.platform == 'win64':
    base = 'Win64GUI'

executables = [Executable(script='poker.py',
                          base=base,
                          targetName='poker.exe')]

setup(name='poker',
      version='0.1',
      description='Sample cx_Freeze wxPython script',
      options={"build_exe" : build_exe_options},
      executables=executables)