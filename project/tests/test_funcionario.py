import pytest
from project.models.funcionario import Funcionario
from project.models.endereco import Endereco

@pytest.fixture
def funcionario_valido():
    funcionario1 = Funcionario("ana", "1111-2222", "ana@gmail.com",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))
    return funcionario1

def test_nome_valido(funcionario_valido):
    assert funcionario_valido.nome == "ana"

def test_telefone_valido(funcionario_valido):
    assert funcionario_valido.telefone == "1111-2222"

def test_email_valido(funcionario_valido):
    assert funcionario_valido.email == "ana@gmail.com"

def test_salario_valido(funcionario_valido):
    assert funcionario_valido.salario == 2000

def test_nome_vazio():
    with pytest.raises(TypeError, match = "Nome não pode ficar vazio!"):
        Funcionario(" ", "1111-2222", "ana@gmail.com",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match = "Nome deve ser um texto!"):
        Funcionario(1, "1111-2222", "ana@gmail.com",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_telefone_vazio():
    with pytest.raises(TypeError, match = "Telefone não pode ficar vazio!"):
        Funcionario("ana", " ", "ana@gmail.com",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_telefone_tipo_invalido():
    with pytest.raises(TypeError, match = "Telefone deve ser um texto!"):
        Funcionario("ana", 1, "ana@gmail.com",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))
    
def test_email_vazio():  
    with pytest.raises(TypeError, match = "Email não pode ficar vazio!"):
        Funcionario("ana", "1111-2222", " ",  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_email_tipo_invalido():  
    with pytest.raises(TypeError, match = "Email deve ser um texto!"):
        Funcionario("ana", "1111-2222", 1,  2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_salario_vazio():
    with pytest.raises(TypeError, match = "Salário não pode ficar vazio!"):
        Funcionario("ana", "1111-2222", "ana@gmail.com",  None, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match = "Salário deve ser números!"):
        Funcionario("ana", "1111-2222", "ana@gmail.com",  "2000", Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))

def test_salario_negativo():
    with pytest.raises(ValueError, match = "Salário não pode ser negativo!"):
        Funcionario("ana", "1111-2222", "ana@gmail.com",  -2000, Endereco("Rua", "1", "Térreo", "11111-22", "São Paulo"))