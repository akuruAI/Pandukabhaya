from setuptools import setup, find_packages

setup(
    name="pandukabhaya",
    version="1.0.1",
    author="akuruAI",
    description="An ASCII to Unicode text converter for 'FM Abhaya' Sinhala font, with extensibility for other fonts via JSON mappings.", # noqa
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/akuruAI/Pandukabhaya",
    include_package_data=True,
    packages=['pandukabhaya'],
    package_dir={'pandukabhaya': 'pandukabhaya'},
    package_data={'pandukabhaya': ['mappings/*.json']},
    install_requires=[],
    entry_points={
        "console_scripts": [
            "pandukabhaya=pandukabhaya.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
