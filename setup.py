import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="test_te_library_4",
    version="2021.10",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maghaali/test_te_library",
    project_urls={
        "Bug Tracker": "https://github.com/maghaali/test_te_library/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'pandas>=1.3.4',
        'numpy>=1.21.3',
        'plotly>=5.3.1'
        ]
)