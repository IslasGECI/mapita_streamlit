from mapita_streamlit import add_captures, update_trap_lines
import pandas as pd

original = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [False, False, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Inactiva", "Inactiva", "Inactiva", "Activa"],
    }
)

line = pd.DataFrame({"line": ["linea 1", "cerco"], "is_active": [True, False]})
expected = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [True, True, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Activa", "Activa", "Inactiva", "Activa"],
    }
)

line_2 = pd.DataFrame({"line": ["linea 1", "cerco"], "is_active": [False, False]})
expected_2 = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [False, False, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Inactiva", "Inactiva", "Inactiva", "Activa"],
    }
)


def test_update_trap_lines():
    obtained = update_trap_lines(original, line)
    assert (obtained.is_active == expected.is_active).all()
    assert (obtained.color == expected.color).all()
    assert (obtained.ID == expected.ID).all()

    obtained = update_trap_lines(original, line_2)
    assert (obtained.is_active == expected_2.is_active).all()


capturas = pd.DataFrame({"ID": [2, 3], "captures": [True, False]})

expected_captures = pd.DataFrame(
    {
        "line": ["linea 1", "linea 1", "cerco", "Linea 2"],
        "is_active": [False, False, False, True],
        "ID": [1, 2, 3, 4],
        "color": ["Inactiva", "Captura", "Inactiva", "Activa"],
    }
)


def test_add_captures():
    obtained = add_captures(original, capturas)
    print(obtained)
    assert (obtained.color == expected_captures.color).all()
