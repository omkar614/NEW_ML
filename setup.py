from setuptools import find_packages,setup
from typing import List


this_text="-e ."

def get_requirements(file_path:str)->List[str]:
    '''this function return list of requiremnt'''
    requirement =[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        if this_text in requirements:
            requirements.remove(this_text)
    return requirements       

setup (
    name = "mlproject",
    version="0.0.1",
    author='Omkar',
    author_email="osawant664@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),


)