from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='ft_package',
    version='0.0.1',
    author='Edouard Flaquet',
    author_email='eflaquet@student.42.fr ',
    long_description=long_description,
    description='A short description of your package',
    python_requires='>=3.6',
    license="MIT",
)
