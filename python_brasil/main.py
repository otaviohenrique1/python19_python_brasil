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

# from datetime import datetime, timedelta
# from datas_br import DatasBr

# hoje = DatasBr()
# print(hoje.tempo_cadastro())

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1)
# print(amanha - hoje)

# hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
# print(hoje)
# print(hoje_formatado)

# numero = 1
# string = "um"
# print(len(string))

from acesso_cep import BuscaEndereco
import requests

# cep = "01001000"
cep = "12630000"
objeto_cep = BuscaEndereco(cep)
# print(objeto_cep)
# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)
a = objeto_cep.acessa_via_cep()
# print(type(r))
# print(dir(r))
# print(type(a.text))
# print(a.json())
# print(a.json()['cep'])
print(a)