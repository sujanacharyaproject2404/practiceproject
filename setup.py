# create a machine learning model as a package.
# from there any body can use install and use it

# it will help to find entire package in the directory
from setuptools import find_packages, setup
from typing import List


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='practiceproject',
version='0.0.1',
author='Sujan',
author_email='sujanacharya024@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)
