from setuptools import setup, find_packages

setup(name="Assignments",
      version="0.1.1",
      packages=find_packages(exclude=["tests"]),
      author="Arden Sinclair",
      description="Assignments for CS30",
      url="https://github.com/ArdenSinclair/CS30-Assignments",
      tests_require=["pytest"])
