from collections.abc import Sequence
import numpy as np

def is_scipy_wav_style(value):
    # If Tuple[int, numpy.ndarray] or not
    return (
        isinstance(value, Sequence)
        and len(value) == 2
        and isinstance(value[0], int)
        and isinstance(value[1], np.ndarray)
    )
