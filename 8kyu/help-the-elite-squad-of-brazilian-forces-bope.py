from typing import Tuple

def mag_number(info: Tuple[str, int]):
    weapons = {"PT92": 17, "M4A1": 30, "M16A2": 30, "PSG1": 5}

    req_ptrs = info[1] * 3
    available_ptrs = weapons[info[0]]
    mags = req_ptrs // available_ptrs
    rem = mags * available_ptrs - req_ptrs

    return mags if rem >= 0 else mags + 1
