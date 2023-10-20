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

[![Test](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/test.yml/badge.svg)](https://github.com/mgao6767/fortran-python-extension-example/actions/workflows/test.yml)

This example is built and tested with Python 3.8 to 3.11, on Ubuntu, Windows and MacOS.
