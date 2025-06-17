from calculator import dodawanie,dzielenie,mnozenie,odejmowanie,create_dataframe,get_dataframe_shape
def test_dodawanie():
    assert dodawanie(2, 3) == 5
    assert dodawanie(-1, 1) == 0

def test_odejmowanie():
    assert odejmowanie(5, 3) == 2
    assert odejmowanie(1, -1) == 2

def test_mnozenie():
    assert mnozenie(2, 3) == 6
    assert mnozenie(-1, 1) == -1

def test_dzielenie():
    assert dzielenie(6, 3) == 2
    assert dzielenie(1, -1) == -1
    assert dzielenie(1, 0) == "Błąd: dzielenie przez zero!"

def test_create_dataframe():
    test_data = {'col1': [1, 2], 'col2': [3, 4]}
    df = create_dataframe(test_data)
    assert isinstance(df, pandas.DataFrame)
    assert not df.empty

def test_get_dataframe_shape():
    test_data = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
    df = pandas.DataFrame(test_data)
    shape = get_dataframe_shape(df)
    assert shape == (3, 2)