import shutil
import os 

shutil.copyfile('lib.py', 'lib_copy.py')
shutil.move('lib_copy.py', './test_dir')