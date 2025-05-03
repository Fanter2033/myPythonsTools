from setuptools import setup, find_packages

setup(
    name="file_transfer",
    version="0.1.2",
    packages=find_packages(),
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": [
            "file_transfer = file_transfer.cli:main",
        ],
    },
)