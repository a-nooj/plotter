import setuptools
from pathlib import Path

setuptools.setup(
    name='plotter',
    author="Anuj Pasricha",
    author_email='anuj.pasricha@colorado.edu',
    version='0.0.1',
    description='A Matplotlib wrapper for generating publication- and presentation- quality plots.',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/a-nooj/plotter',
    packages=setuptools.find_packages(where='plotter*'),
    install_requires=['numpy==1.19', 'matplotlib==3.3.0'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        ],
    python_requires='>=3.6'
)

