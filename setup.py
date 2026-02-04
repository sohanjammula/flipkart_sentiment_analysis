from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    requiremnts = []
    with open(file_path) as file_obj:
        requiremnts = file_obj.readlines()
        requiremnts = [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requiremnts:
            requiremnts.remove(HYPHEN_E_DOT)
        return requiremnts

setup(
    name = 'flipkartSentimentAnalysis'
    version= 0.0.1
    author='J.V.S SOHAN'
    author_email="sohan.jammula123@gmail.com"
    install_requires = get_requirements('requirement.txt')
    packages = find_packages()
)