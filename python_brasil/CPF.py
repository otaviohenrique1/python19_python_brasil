from validate_docbr import CPF as validadorCPF

class CPF:
    def __init__(self, documento: int | str):
        documento = str(documento)
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF inválido!")

    def __str__(self):
        return self.format_cpf()

    def cpf_e_valido(self, cpf: str):
        if len(cpf) == 11:
            validador = validadorCPF()
            return validador.validate(cpf)
        else:
            raise ValueError("Quantidade de digitos inválida!!")

    def format_cpf(self):
        mascara = validadorCPF()
        return mascara.mask(self.cpf)
        # fatia_um = self.cpf[:3]
        # fatia_dois = self.cpf[3:6]
        # fatia_tres = self.cpf[6:9]
        # fatia_quatro = self.cpf[9:]
        # return "{}.{}.{}-{}".format(
        #     fatia_um,
        #     fatia_dois,
        #     fatia_tres,
        #     fatia_quatro,
        # )
