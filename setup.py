from setuptools import setup, find_packages

VERSION = '0.0.4'
DESCRIPTION = "Just playing around"
LONG_DESCRIPTION = 'Just playing around in long description'

# Setting up
setup(
    name="testplay",
    version=VERSION,
    author="Darsh (Subhash Mishra)",
    author_email="subhashmishra4322@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[], # for installing dependencies
    keywords=[], #for keywords for your projects.
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)