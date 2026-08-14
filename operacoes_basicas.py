# -------------------------
# 1. Operações Aritméticas
# -------------------------

print("--- Operações Aritméticas ---")

valor_a = 25
valor_b = 4

soma_resultado = valor_a + valor_b
sub_resultado = valor_a - valor_b
multi_resultado = valor_a * valor_b
div_resultado = valor_a / valor_b
div_inteira_resultado = valor_a // valor_b
resto_resultado = valor_a % valor_b
potencia_resultado = valor_a ** valor_b

print(f"{valor_a} + {valor_b} = {soma_resultado}")
print(f"{valor_a} - {valor_b} = {sub_resultado}")
print(f"{valor_a} * {valor_b} = {multi_resultado}")
print(f"{valor_a} / {valor_b} = {div_resultado}")
print(f"{valor_a} // {valor_b} = {div_inteira_resultado}")
print(f"{valor_a} % {valor_b} = {resto_resultado}")
print(f"{valor_a} ** {valor_b} = {potencia_resultado}")

print("-" * 20)


# -------------------------
# 2. Operações com Strings
# -------------------------

print("--- Operações com Strings ---")

nome_usuario = "Lucas"
sobrenome_usuario = "Costa"

nome_completo_usuario = nome_usuario + " " + sobrenome_usuario

print(f"Nome completo: {nome_completo_usuario}")

palavra = "Olá "
mensagem_repetida = palavra * 3

print(f"Mensagem: {mensagem_repetida}")

print("-" * 20)


# -------------------------
# 3. Operações de Comparação
# -------------------------

print("--- Operações de Comparação ---")

idade_pessoa = 18
idade_minima = 21

print(f"As idades são iguais? {idade_pessoa == idade_minima}")
print(f"As idades são diferentes? {idade_pessoa != idade_minima}")
print(f"A primeira idade é maior? {idade_pessoa > idade_minima}")
print(f"A primeira idade é menor? {idade_pessoa < idade_minima}")
print(f"A primeira idade é maior ou igual? {idade_pessoa >= idade_minima}")
print(f"A primeira idade é menor ou igual? {idade_pessoa <= idade_minima}")

print("-" * 20)


# -------------------------
# 4. Operações Lógicas
# -------------------------

print("--- Operações Lógicas ---")

tem_passagem = True
documento_pronto = True

pode_embarcar = tem_passagem and documento_pronto
pode_entrar = tem_passagem or documento_pronto
documento_pendente = not documento_pronto

print(f"Pode embarcar? {pode_embarcar}")
print(f"Pode entrar? {pode_entrar}")
print(f"Documento está pendente? {documento_pendente}")

print("-" * 20)
