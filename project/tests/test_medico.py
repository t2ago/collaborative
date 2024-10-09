import pytest
from project.models.medico import Medico
from project.models.endereco import Endereco

@pytest.fixture
def medico_valido():
    medico = Medico("ana", "1111-2222", "ana@gmail.com",  4000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), "222")
    return medico

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "222"

def test_crm_vazio():
    with pytest.raises(TypeError, match = "CRM não pode ficar vazio!"):
        Medico("ana", "1111-2222", "ana@gmail.com",  4000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), " ")

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match = "CRM deve ser um texto!"):
        Medico("ana", "1111-2222", "ana@gmail.com",  4000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"), 222)