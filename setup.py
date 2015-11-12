from setuptools import setup

setup(
    name="gofigure",
    version="0.0",

    packages=[
        "gofigure",
        "gofigure/components",
        "gofigure/parsers"
    ],
    scripts=[],

    package_data = {
        "": ["static/*", "static/*/*", "static/*/*/*"] # ...
    }
)
