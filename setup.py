from setuptools import find_packages
from numpy.distutils.core import setup, Extension

mod_fort = Extension(
    "fortext.algo.math",
    sources=["src/fortext/algo/math.f90"],
    language="fortran",
)

ext_modules = [mod_fort]

setup(
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    ext_modules=ext_modules,
)
