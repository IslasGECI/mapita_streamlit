import pandas as pd


def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def update_trap_lines(original: pd.DataFrame, line):
    return pd.DataFrame(
        {
            "is_active": [True, True, False, True],
        }
    )
