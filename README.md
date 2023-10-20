# Fortran Python extension example

This is a minimal working example for using Fortran to write Python extension.

`src\fortext\algo\math.f90` contains a Fortran subroutine `factorial`.

We are to compile `math.f90` into an extension `fortext.algo.math`.

```bash
pip install .
```

Then, we can use `math.factorial()` as:

```python
from fortext.algo import math

print(math.factorial(5))
```

## Build Status

This example is built and tested with Python 3.8 to 3.11, on Ubuntu, Windows and MacOS.

| OS      | Status                                                                                                                                                                                                                     |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Ubuntu  | [![Ubuntu](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-Ubuntu.yml/badge.svg)](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-Ubuntu.yml)    |
| Windows | [![Windows](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-Windows.yml/badge.svg)](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-Windows.yml) |
| MacOS   | [![MacOS](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-MacOS.yml/badge.svg)](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/Build-MacOS.yml)       |
