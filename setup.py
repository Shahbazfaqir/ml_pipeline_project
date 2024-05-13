from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    requirements= []

    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPHON_E_DOT in requirements:
            requirements.remove(HYPHON_E_DOT)

    

setup(
    name="ML_Pipeline_Project",
    version="0.0.1",
    description="Machine Learning Pipeline Project",
    author="shahbaz faqir",
    author_email="shabaz.h000pm@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)