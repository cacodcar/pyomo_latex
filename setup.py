"""
pyomo_latex setup file
"""

from setuptools import setup, find_packages

__version__ = "1.0.0"

short_desc = (
    "Generates latex equations from pyomo equations"
)


def setup_package():
    """
    sets up pyomo_latex
    """
    with open('README.md', encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='pyomo_latex',
        version=__version__,
        author='Rahul Kakodkar',
        author_email='cacodcar@gmail.com',
        description=short_desc,
        long_description=long_description,
        long_description_content_type="text/markdown",
        license='MIT',
        url='https://github.com/cacodcar/pyomo_latex',
        install_requires=[
            'inspect'
        ],
        packages=find_packages(where='pyomo_latex'),
        package_dir={'': 'pyomo_latex'},
    )


if __name__ == '__main__':
    setup_package()