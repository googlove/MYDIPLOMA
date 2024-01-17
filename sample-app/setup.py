from os import path

from setuptools import setup

here = path.abspath(path.dirname(__file__))

setup(
    name='cat-translator',
    version='1.0.0',
    description='Python Flask app for classifying cat vocalization using a trained Visual Recognition model on IBM '
                'Cloud',
    license='Apache-2.0'
)
