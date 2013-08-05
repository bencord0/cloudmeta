import os
from setuptools import setup, find_packages

os.chdir(os.path.dirname(os.path.abspath(os.path.normpath(__file__))))

setup(name='cloudmeta',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'cloudmeta = cloudmeta.wsgi:main'
            ]
        }
)
