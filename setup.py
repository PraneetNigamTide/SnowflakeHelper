from setuptools import setup, find_packages

setup(
    name="snowflake-conn",
    version="0.7.0",
    description="A Python package for interacting with Snowflake using PySpark",
    author="Praneet Nigam",
    author_email="praneet.nigamil@tide.co",
    url="https://github.com/yourusername/snowflake-conn",
    packages=find_packages(),
    install_requires=[
        "pyspark",
        "snowflake-connector-python",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)