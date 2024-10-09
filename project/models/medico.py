from project.models.funcionario import Funcionario
from project.models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, salario, endereco)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,valor):
        self._verificar_crm_tipo_invalido(valor)
        self._verificar_crm_vazio(valor)

        self.crm = valor
        return self.crm
    

    def _verificar_crm_vazio(self, valor):
        if not valor.strip():
            raise TypeError("O CRM não pode ficar vazio!")

    def _verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("O CRM deve ser um texto!")


    def __str__(self) -> str:
        return (
                f"{super().__str__()}"
                f"\nCRM: {self.crm}"
                ) 
    
