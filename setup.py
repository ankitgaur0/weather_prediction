from setuptools import setup,find_packages
from typing import List

HYPEN_e_DOT ="-e ."
def get_requirements(file_path:str)-> List[str]:

    """this function is used for iterate the packages from the Requirements.txt file and then install after return to the install_requires in the setup function """
    Requirements=[]
    with open(file_path) as file_obj:
        Requirements=file_obj.readlines()

        #now replace the "\n" with blank
        Requirements=[req.replace("\n","") for req in Requirements]

        #now remove the -e . from the list
        if HYPEN_e_DOT in Requirements:
            Requirements.remove(HYPEN_e_DOT)

    return Requirements



setup(
    name="weather_prediction",
    version='0.0.1',
    author="ankit",
    author_email="ankitparahar000@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("Requirements.txt")
)