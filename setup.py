from setuptools import setup, find_packages

setup(
    name="COMBO",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gputil",
        "psutil",
        "simanneal==0.4.2",
        "toposort",
        "torch==1.6.0",
        "torchvision==0.7.0",
    ],
    author="QUVA-Lab",
    description="Combinatorial Bayesian Optimization Using the Graph Cartesian Product",
    url="https://github.com/johnswyou/COMBO",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
