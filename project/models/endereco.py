class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)

    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)
        self._verificar_logradouro_vazio(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_numero(self, valor):
        self._verificar_numero_tipo_invalido(valor)
        self._verificar_numero_vazio(valor)
        
        self.numero = valor
        return self.numero
    
    def _verificar_complemento(self, valor):
        self._verificar_complemento_tipo_invalido(valor)
        self._verificar_complemento_vazio(valor)

        self.complemento = valor
        return self.complemento
    
    def _verificar_cep(self, valor):
        self._verificar_cep_tipo_invalido(valor)
        self._verificar_cep_vazio(valor)

        self.cep = valor
        return self.cep
    
    def _verificar_cidade(self, valor):
        self._verificar_cidade_tipo_invalido(valor)
        self._verificar_cidade_vazio(valor)

        self.cidade = valor
        return self.cidade
    
    def _verificar_logradouro_vazio(self, valor):
        if not valor.strip():
            raise TypeError("Logradouro não pode ficar vazio!")
        
    def _verificar_logradouro_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Logradouro deve ser um texto!")

    def _verificar_numero_vazio(self, valor):
        if not valor.strip():
            raise TypeError("Número não pode ficar vazio!")
        
    def _verificar_numero_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Número deve ser um texto!")

    def _verificar_complemento_vazio(self, valor):
        if not valor.strip():
            raise TypeError("Complemento não pode ficar vazio!")

    def _verificar_complemento_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Complemento deve ser um texto!")

    def _verificar_cep_vazio(self, valor):
        if not valor.strip():
            raise TypeError("CEP não pode ficar vazio!")

    def _verificar_cep_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("CEP deve ser um texto!")
        
    def _verificar_cidade_vazio(self, valor):
        if not valor.strip():
            raise TypeError("Cidade não pode ficar vazio!")

    def _verificar_cidade_tipo_invalido(self, valor):
        if not isinstance(valor, str):
            raise TypeError("Cidade deve ser um texto!")

    def __str__(self) -> str:
        return (
                f"\nLogradouro: {self.logradouro}"
                f"\nNumero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCEP: {self.cep}"
                f"\nCidade: {self.cidade}"
                )