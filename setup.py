from setuptools import setup

setup(
    name="metadata-generator-py",
    version="0.1",
    description="Generate that meta data instead of typing it out every time",
    url="https://github.com/mitchthorson/metadata-generator-py",
    author="Mitchell Thorson",
    author_email="mitch.thorson@gmail.com",
    license="MIT",
    packages=["generator"],
    zip-safe=False,
    entry_points = {
        'console_scripts': ['metadata-generator=generator.command_line:run'],
    }
)
