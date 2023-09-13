#!/usr/bin/env python3

from setuptools import find_packages, setup

with open('README.rst', 'r') as file:
    long_description = file.read()

setup(
    name='battlib',
    version='0.0.0',
    description='A library for battery SOC calculation using EKF',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/blueskysolarracing/battlib',
    author='Blue Sky Solar Racing',
    author_email='blueskysolar@studentorg.utoronto.ca',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Topic :: Education',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    keywords=[
        'python',
    ],
    project_urls={
        'Documentation': 'https://battlib.readthedocs.io/en/latest/',
        'Source': 'https://github.com/blueskysolarracing/battlib',
        'Tracker': 'https://github.com/blueskysolarracing/battlib/issues',
    },
    package_data={'battlib': ['py.typed']},
    packages=find_packages(),
    python_requires='>=3.11',
)
