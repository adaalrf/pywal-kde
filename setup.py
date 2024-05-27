from setuptools import setup, find_packages

setup(
    name="pywal",
    version="3.3.0",
    description="Generate and change color-schemes on the fly.",
    url="https://github.com/dylanaraps/pywal",
    author="Dylan Araps",
    author_email="dylan@dylanaraps.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "colorz",
        "image",
        "pillow",
        "requests",
        "dbus-python",
    ],
    entry_points={
        "console_scripts": [
            "wal = pywal.__main__:main",
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

