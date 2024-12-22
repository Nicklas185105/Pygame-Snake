from setuptools import setup, find_packages

setup(
    name="pygame-snake",
    version="0.1",
    packages=find_packages(include=["core", "snake", "snake.*"]),
)
