from setuptools import setup, find_packages

install_requires = [
    'flowit>=1.0.0'
]

setup(
    name="flowit_libs",
    version="1.0.0",
    author="Barak David",
    license="MIT",
    keywords="Extension for flowit library.",
    packages=find_packages(),
    install_requires=install_requires,
    python_requires='>=3'
)