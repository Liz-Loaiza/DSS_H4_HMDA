from setuptools import find_packages
from distutils.core import setup


# Configurando
setup(

        name="snowflake", 
        version="0.1",
        author="Liceth Loaiza",
        author_email="<liceth.t.loaiza@gmail.com>",
        description="Mi first python package",
        packages=find_packages(),
        install_requires=["numpy","turtles"], 
)