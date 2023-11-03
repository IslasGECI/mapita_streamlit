from mapita_streamlit import update_trap_lines
import pandas as pd


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


def test_update_trap_lines():
    obtained = update_trap_lines(original, line)
    assert (obtained.is_active == expected.is_active).all()
    assert (obtained.color == expected.color).all()
