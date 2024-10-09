import pytest
from project.models.engenheiro import Engenheiro
from project.models.endereco import Endereco

@pytest.fixture
def engenheiro_valido():
    engenheiro1 = Engenheiro("ana", "1111-2222", "ana@gmail.com",  3000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), "111")
    return engenheiro1

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "111"

def test_crea_vazio():
    with pytest.raises(TypeError, match = "CREA não pode ficar vazio!"):
        Engenheiro("ana", "1111-2222", "ana@gmail.com",  3000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), " ")

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match = "CREA deve ser um texto!"):
        Engenheiro("ana", "1111-2222", "ana@gmail.com",  3000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), 111)