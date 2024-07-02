# from cpf_cnpj import Documento

# exemplo_cnpj = "43710625000150"
# exemplo_cpf = "14904017099"
# documento1 = Documento.cria_documento(exemplo_cnpj)
# documento2 = Documento.cria_documento(exemplo_cpf)
# print(documento1)
# print(documento2)

# import re

# padrao_molde = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto = "eu gosto do numero 2126451234"
# resposta = re.findall(padrao, texto)
# print(resposta)

# from TelefonesBr import TelefonesBr
# import re

# telefone = "552126481234"
# telefone_objeto = TelefonesBr(telefone)
# print(telefone_objeto)

from datetime import datetime, timedelta
from datas_br import DatasBr

cadastro = DatasBr()
print(cadastro.dia_semana())