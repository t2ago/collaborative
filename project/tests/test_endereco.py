import pytest
from project.models.endereco import Endereco

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo")
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "1"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Térreo"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "11111-22"

def test_cidade_valida(endereco_valido):
    assert endereco_valido.cidade == "São Paulo"

def test_logradouro_vazio():
    with pytest.raises(TypeError, match = "Logradouro não pode ficar vazio!"):
       Endereco(" ", "1", "Térreo", "11111-22", "São Paulo") 

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match = "Logradouro deve ser um texto!"):
       Endereco(1, "1", "Térreo", "11111-22", "São Paulo") 

def test_numero_vazio():
    with pytest.raises(TypeError, match = "Número não pode ficar vazio!"):
        Endereco("Rua", " ", "Térreo", "11111-22", "São Paulo")

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match = "Número deve ser um texto!"):
        Endereco("Rua", 1, "Térreo", "11111-22", "São Paulo")

def test_complemento_vazio():
    with pytest.raises(TypeError, match = "Complemento não pode ficar vazio!"):
        Endereco("Rua", "1", " ", "11111-22", "São Paulo")

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match = "Complemento deve ser um texto!"):
        Endereco("Rua", "1", 1, "11111-22", "São Paulo")

def test_cep_vazio():
    with pytest.raises(TypeError, match = "CEP não pode ficar vazio!"):
        Endereco("Rua", "1", "Térreo", " ", "São Paulo")

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match = "CEP deve ser um texto!"):
        Endereco("Rua", "1", "Térreo", 1, "São Paulo")

def test_cidade_vazio():
    with pytest.raises(TypeError, match = "Cidade não pode ficar vazio!"):
        Endereco("Rua", "1", "Térreo", "11111-22", " ")

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match = "Cidade deve ser um texto!"):
        Endereco("Rua", "1", "Térreo", "11111-22", 1)