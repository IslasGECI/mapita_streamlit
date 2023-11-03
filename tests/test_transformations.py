import mapita_streamlit as dt
import pandas as pd


def test_add_offset():
    augend = 1
    addend = 2
    expected = augend + addend
    obtained = dt.add_offset(augend, addend)
    assert expected == obtained


line = pd.DataFrame({"line": ["linea 1", "cerco"], "is_active": [True, False]})
original = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [False, False, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Inactiva", "Inactiva", "Inactiva", "Activa"],
    }
)
expected = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [True, True, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Activa", "Activa", "Inactiva", "Activa"],
    }
)
