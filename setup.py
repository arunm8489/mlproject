## setup.py - to build our application as a package itself
from setuptools import find_packages,setup 
from typing import List
## find_packages will fetch folders containing __init__.py 
## and considers them as folders


def get_requirements(file_path: str)->List[str]:
    '''
    this function will return list of requirements
    '''
    requirements = []
    with open(file_path) as f_obj:
        requirements = f_obj.readlines()
        requirements = [f.replace("\n","") for f in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
name='mlproject',
version='0.0.1',
author='arun',
author_email='arunm8489@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)