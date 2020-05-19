import setuptools
import os

setuptools.setup(
    name="vae",
    version="0.1.0",
    author="Zapata Computing, Inc.",
    author_email="info@zapatacomputing.com",
    description="Variational autoencoders.",
    packages= setuptools.find_packages(where = "python"),
    package_dir={'' : 'python'},
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "torch",
        "torchvision",
        "numpy"
    ]
)
