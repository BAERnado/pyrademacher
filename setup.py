import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrademacher",
    version="0.13.1",
    author="Pedro Ribeiro",
    author_email="pedroeusebio@gmail.com",
    description="Control devices connected to your Rademacher Homepilot "
    "(or Start2Smart) hub",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/peribeir/pyrademacher",
    project_urls={
        "Bug Tracker": "https://github.com/peribeir/pyrademacher/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
    install_requires=["aiohttp~=3.8.1"]
)
