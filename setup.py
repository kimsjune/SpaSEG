from setuptools import setup, find_packages

setup(
    name="spaseg",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pytorch==1.12.0",
        "opencv-python==4.7.0",
        "squidpy==1.2.3",
        "cell2location==v0.8a0",
        "scanpy>=1.9.1",
        "pandas>=1.5.1",
        "numpy>=1.22.4",
        "matplotlib>=3.6.0",
        "seaborn>=0.11.0",
        "sklearn>=1.2.2",
        "shapely==2.0.1",
        "numba>=0.55.2",
        "statsmodels==0.14.0"

    ]
)