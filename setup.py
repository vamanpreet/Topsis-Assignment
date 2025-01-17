from setuptools import setup, find_packages # type: ignore

setup(
    name="Topsis-Vamanpreet-102217011",
    version="0.1.0",
    author="Vamanpreet Kaur",
    author_email="vamanpreet2110@gmail.com",
    description="A Python package to perform Topsis analysis.",
    url="https://github.com/vamanpreet/Topsis-Assignment",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
