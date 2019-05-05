import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="creativity",
    version="0.0.2",
    author="Arlan Jaska",
    author_email="akjaska@gmail.com",
    description="Quick inspiration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajaska/creativity",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Artistic Software",
    ],
)
