from setuptools import setup, find_namespace_packages

setup(
    name='For clean folder',
    version='1.0.21',
    description='Very useful code',
    url='http://github.com/IevgenSharnin/HomeWork7',
    author='Ievgen Sharnin',
    author_email='83iwert@gmail.com',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.sort:run']})