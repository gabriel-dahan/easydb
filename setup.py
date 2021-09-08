import setuptools

setuptools.setup(
    name = "easypsql",
    version = "1.0",
    author = "Gabriel D.",
    description = "A package allowing you to interact with PostgreSQL a simpler way in python.",
    url = "https://github.com/gabriel-dahan/psql-easyconn",
    packages = setuptools.find_packages(),
    python_requires = '>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3"
    ]
)