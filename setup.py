from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in safety/__init__.py
from safety import __version__ as version

setup(
	name='safety',
	version=version,
	description='Safety',
	author='Cosumar Digital Factory',
	author_email='support@cosumar.app',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
