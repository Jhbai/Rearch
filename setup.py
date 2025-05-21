from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

extensions = [
    Extension(
        name="pelt_segmentation",
        sources=["pelt_segmentation.pyx", "_pelt.c"],
        include_dirs=[np.get_include()],
    )
]

setup(
    name="pelt_segmentation",
    ext_modules=cythonize(extensions),
)
