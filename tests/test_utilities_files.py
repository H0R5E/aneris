# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 17:28:04 2015

@author: 108630
"""

import os

from aneris.utilities.files import mkdir_p

def test_mkdir_p(tmpdir):
    
    test_dir_name = "test"
    test_path = os.path.join(str(tmpdir), test_dir_name)
    mkdir_p(test_path)
    
    assert os.path.isdir(test_path)
    