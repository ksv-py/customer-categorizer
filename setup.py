from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    
    requirements = []
    with open(file_path, 'r') as file_obj:
        lines = file_obj.readlines()

        requirements = [req.strip() for req in lines]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name="customer-categorizer",
    version="0.0.1",
    author="Keshav Jangid",
    author_email="keshavjangid301@gmail.com",
    description="A tool for customer categorization",
    long_description=open('README.md').read(),
    url="",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",   
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=get_requirements('requirements.txt'),
    # entry_points={
    #     'console_scripts': [
    #         'customer-categorizer = '
    #     ]
    # }
)