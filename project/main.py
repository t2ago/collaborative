import sys
sys.path.append('/workspaces/collaborative')

from project.models.endereco import Endereco
from project.models.funcionario import Funcionario
from project.models.engenheiro  import Engenheiro
from project.models.medico import Medico

funcionario = Funcionario("a", "1111-2222", "a@gmail.com", 2000, Endereco("Rua A", "11", "Térreo", "11111-22", "São Paulo"))
engenheiro = Engenheiro("b", "3333-4444", "b@gmail.com", 3000, Endereco("Rua B", "22", "1º Andar", "33333-44", "São Paulo"), "111")
medico = Medico("c", "5555-6666", "c@gmail.com", 4000, Endereco("Rua C", "33", "2º Andar", "55555-66", "São Paulo"), "222")

print(funcionario)
print(engenheiro)
print(medico)