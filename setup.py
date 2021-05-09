import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygame-animations", # Replace with your own username
    version="1.1.0",
    author="K_39",
    author_email="louisdevie@gmail.com",
    description="An extension for pygame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k39dev/pygame-animations",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=['pygame>=2.0.0'],
)