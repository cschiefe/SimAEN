#!/usr/bin/env python

# -*- coding: utf-8 -*-
# DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited.

# This material is based upon work supported under Air Force Contract No. FA8702-15-D-0001.
# Any opinions,findings, conclusions or recommendations expressed in this material are those
# of the author(s) and do not necessarily reflect the views of the Centers for Disease Control.

# (c) 2021 Massachusetts Institute of Technology.

# The software/firmware is provided to you on an As-Is basis

# Delivered to the U.S. Government with Unlimited Rights, as defined in DFARS Part 252.227-7013
# or 7014 (Feb 2014). Notwithstanding any copyright notice, U.S. Government rights in this work
# are defined by DFARS 252.227-7013 or DFARS 252.227-7014 as detailed above. Use of this work
# other than as specifically authorized by the U.S. Government may violate any copyrights that
# exist in this work.

# Copyright (c) 2021 Massachusetts Institute of Technology
# SPDX short identifier: MIT

# Developed as part of: SimAEN, 2021

import os

from setuptools import setup, find_packages

setup(name='simaen_api',
      version='0.1.0',
      description='SIMAEN REST API',
      author='MIT Lincoln Laboratory',
      classifier=['Private :: Do Not Upload'],
      license="This software is provided on an As-Is basis.",
      entry_points={
          'console_scripts': [
              'simaen = simaen_api.__main__:main'
          ]
      },
      package_dir={'simaen_api': 'simaen_api'},
      package_data={'': [os.path.join('resources', '*'), os.path.join('resources', '.*')]},
      packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
      install_requires=[
        'dask',
        'requests',
        'flask',
        # 'flask-session',
        'flask-restx',
        'flask-socketIO',
        'flask-httpauth',
        'flask-cors',
        'psutil',
        'argparse', 
        'pydotplus',
      ],
      extras_require={
        'docs': [
            'Sphinx==1.3.6',
            'docutils==0.12',
            'sphinx_py3doc_enhanced_theme==2.3.2',
            'sphinx-pypi-upload==0.2.1',
        ]
      } 
)
