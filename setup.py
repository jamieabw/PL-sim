from setuptools import setup, find_packages

setup(
    name="pl-predictor",            # any name you like for the project
    version="0.1.0",
    package_dir={"": "src"},        # << tell setuptools code is in src/
    packages=find_packages("src"),  # << find all packages under src/
    python_requires=">=3.10",
)