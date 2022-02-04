from setuptools import setup
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
README = (BASE_DIR / "README.md").read_text()

setup(
    name="glrlm",
    version="0.1.0",
    author="M Razif Rizqullah",
    author_email="razifrizqullah@gmail.com",
    url='https://github.com/eiproject/python-glrlm',
    description="Gray Level Run Length Matrix",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=['glrlm'],
    include_package_data=True,
    install_requires=[
            'numpy',
            'opencv-python'
            ],
    keywords=['python', 'glrlm', 'feature extraction', 'image processing'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)


# python setup.py sdist bdist_wheel
# twine upload dist/*