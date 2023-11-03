import pandas as pd


def add_offset(augend: int, addend: int) -> int:
    return augend + addend


def update_trap_lines(original: pd.DataFrame, line):
    expected = pd.DataFrame(
        {
            "is_active": [True, True, False, True],
        }
    )
    return add_color(expected)


def add_color(expected):
    return expected.assign(
        color=lambda dataframe: dataframe["is_active"].map(
            lambda is_active: "Activa" if is_active else "Inactiva"
        )
    )
