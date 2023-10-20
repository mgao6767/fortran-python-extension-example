# Fortran Python extension example

This is a minimal working example for using Fortran to write Python extension.

`src\fortext\algo\math.f90` is contains a Fortran subroutine `factorial`.

We are to compile `math.f90` into an extension `fortext.algo.math`.

```bash
pip install .
```

Then, we can use `math.factorial()` as:

```python
from fortext.algo import math

print(math.factorial(5))
```
