from project.models.funcionario import Funcionario
from project.models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)
        self._verificar_crea_vazio(valor)

        self.crea = valor
        return self.crea
    
    def _verificar_crea_vazio(self, valor):
        if not valor.strip():
            raise TypeError("CREA não pode ficar vazio!")

    def _verificar_crea_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("CREA deve ser um texto!")

    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"\nCREA: {self.crea}"
                )