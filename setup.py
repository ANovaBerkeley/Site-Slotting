from setuptools import setup, find_packages

setup(
    name="site-slotting",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        "numpy",
        "pandas",
        "ipykernel",
        "tqdm",
    ],
    tests_require=[
        # List your test dependencies here
        "pytest",
    ],
    entry_points={
        "console_scripts": [
            "my_script = site-slotting.script:main",
        ],
    },
    author="Jacob Aldrich",
    author_email="executive@anova.berkeley.edu",
    description="This code is meant to place old and new members at Berkeley ANovas various sites.",
    long_description="This code is meant to do two things: 1. Put old members into sites given a .csv file of their preferences. 2. Place new members into sites given a .csv file of their preferences, taking into account old members already being placed at a site a couple of weeks ago.",
    long_description_content_type="text/markdown",
    url="https://github.com/ANovaBerkeley/Site-Slotting",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
