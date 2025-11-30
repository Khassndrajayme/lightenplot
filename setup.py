"""
Setup configuration for PlotEase package
"""

from setuptools import setup, find_packages
import os

# Read the README file for long description
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()

# Read requirements from requirements.txt
def read_requirements():
    with open('requirements.txt', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    # Package metadata
    name='plotease',
    version='1.0.0',
    author='Your Team Name',
    author_email='your.email@example.com',
    description='A simplified data visualization library for Python',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/plotease',
    
    # Package configuration
    packages=find_packages(exclude=['tests', 'docs', 'examples']),
    python_requires='>=3.8',
    
    # Dependencies
    install_requires=read_requirements(),
    
    # Package classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    
    # Keywords for PyPI search
    keywords='visualization plotting data-science matplotlib seaborn oop',
    
    # Project URLs
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/plotease/issues',
        'Source': 'https://github.com/yourusername/plotease',
        'Documentation': 'https://plotease.readthedocs.io/',
    },
    
    # Include additional files
    include_package_data=True,
    package_data={
        'plotease': ['data/*.csv'],
    },
    
    # Entry points (optional - for command-line tools)
    # entry_points={
    #     'console_scripts': [
    #         'plotease=plotease.cli:main',
    #     ],
    # },
    
    # Zip safe
    zip_safe=False,
)
