from setuptools import setup, find_packages

setup(
    name='eniac',
    version='0.1.0',
    packages=find_packages(include='__init__'),
    install_requires=open('requirements.txt', 'r'),
    entry_points={
	'console_scripts': ['eniac=__init__']
},
)
