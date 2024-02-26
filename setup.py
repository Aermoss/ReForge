from setuptools import setup

import os, sys, reforge

with open("README.md", "r", encoding = "UTF-8") as file:
    longDesc = file.read()

with open("requirements.txt", "w", encoding = "UTF-8") as file:
    file.write("\n".join(reforge.__requirements__))

setup(
    name = "reforge",
    packages = ["reforge"],
    version = reforge.__version__,
    entry_points = {
        "console_scripts": []
    },
    description = longDesc.split("\n")[1],
    long_description = longDesc,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Aermoss/ReForge",
    author = reforge.__author__,
    author_email = "aermoss.0@gmail.com",
    license = "MIT",
    keywords = [],
    include_package_data = True,
    install_requires = reforge.__requirements__
)