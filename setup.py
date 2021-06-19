import pathlib
from setuptools import setup,find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="dataframe-to-image",
    version="0.0.1",
    description="Convert Pandas DataFrame to Image",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/imaadmkhan1/dataframe_to_image",
    author="Imaad Mohamed Khan",
    author_email="imaadmkhan1@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["pandas", "numpy","matplotlib","plotly"]
)