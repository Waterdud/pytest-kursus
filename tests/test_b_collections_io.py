import pytest
from src.b_collections_io import (
    unique_sorted, count_words, merge_dicts, find_max_pair, flatten,
    read_file, write_file, safe_get, top_n, chunk_list
)

# B-OSA TESTID: Kirjuta teste, et leida vigased funktsioonid!
# Järgmised 2 testi on näited - kirjuta ülejäänud testid ise!

def test_unique_sorted_basic():
    """Test unikaalsete sorteeritud arvude funktsiooni."""
    assert unique_sorted([3,1,2,2,3]) == [1,2,3]
    assert unique_sorted([]) == []
    assert unique_sorted([5,5,5]) == [5]

def test_count_words_basic():
    """Test sõnade loendamise funktsiooni."""
    text = "tere tere tulemast koju"
    out = count_words(text)
    assert out == {"tere": 2, "tulemast": 1, "koju": 1}

def merge_dicts_basic():
    """Test sõnastike ühendamise funktsiooni."""
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 3, 'c': 4}
    out = merge_dicts(d1, d2)
    assert out == {'a': 1, 'b': 3, 'c': 4}

def test_find_max_pair_basic():
    """Test maksimumi ja selle sageduse leidmise funktsiooni."""
    assert find_max_pair([1,3,2,3,1]) == (3, 2)
    with pytest.raises(ValueError):
        find_max_pair([])

def test_flatten_basic():
    """Test lamedaks tegemise funktsiooni."""
    assert flatten([[1,2], [3,4]]) == [1,2,3,4]
    assert flatten([]) == [] 
    assert flatten([[1], [], [2,3]]) == [1,2,3]

def test_read_file_basic(tmp_path):
    """Test faili lugemise funktsiooni."""
    file_path = tmp_path / "test.txt"
    file_path.write_text("Hello, world!", encoding='utf-8')
    assert read_file(file_path) == "Hello, world!"

def test_write_file_basic(tmp_path):
    """Test faili kirjutamise funktsiooni."""
    file_path = tmp_path / "output.txt"
    text = "Sample text"
    num_chars = write_file(file_path, text)
    assert num_chars == len(text)
    assert file_path.read_text(encoding='utf-8') == text

def test_safe_get_basic():
    """Test turvalise võtme saamise funktsiooni."""
    d = {'x': 10, 'y': 20}
    assert safe_get(d, 'x') == 10
    assert safe_get(d, 'z', default=0) == 0
    assert safe_get(d, 'y', default=5) == 20

def test_top_n_basic():
    """Test suurimate n arvude leidmise funktsiooni."""
    assert top_n([1,3,2,5,4], 3) == [5,4,3]
    with pytest.raises(ValueError):
        top_n([1,2], 0)
    with pytest.raises(ValueError):
        top_n([1,2], 3)

def test_chunk_list_basic():
    """Test listi tükeldamise funktsiooni."""
    assert chunk_list([1,2,3,4,5], 2) == [[1,2], [3,4], [5]]
    assert chunk_list([1,2,3], 3) == [[1,2,3]]
    assert chunk_list([], 1) == []
    with pytest.raises(ValueError):
        chunk_list([1,2,3], 0)



# TODO: Kirjuta ülejäänud testid ise!
# Vihje: mõned funktsioonid on vigased - sinu testid peaksid need leidma!
