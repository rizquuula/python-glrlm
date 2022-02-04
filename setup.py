from telnetlib import Telnet
from setuptools import setup
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / "README.md").read_text()

setup(
    name="glrlm",
    version="0.1.0",
    author="M Razif Rizqullah",
    author_email="razifrizqullah@gmail.com",
    description="Gral Level Run Length Matrix",
    long_description=README,
    license='MIT',
    packages=['glrlm'],
    include_package_data=True,
    install_requires=[],
    keywords=['python', 'glrlm', 'feature extraction'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)