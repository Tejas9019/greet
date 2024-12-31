from setuptools import setup, find_packages

setup(
    name="greet",  # Unique name for your library
    version="0.1.0",  # Initial version
    author="Tejas",
    author_email="tejasd603@gmail.com",
    description="A simple Python library example",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Tejas9019/greet.git",  # Replace with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
