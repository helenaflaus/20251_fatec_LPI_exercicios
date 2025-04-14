from ex16 import confere_senha

# 1. Menos de 12 caracteres
print(1)
confere_senha('A1b@')  
# inválida

# 2. Sem número suficiente
print(2)
confere_senha('Abcdefghijk!@')  
# inválida

# 3. Sem letra maiúscula suficiente
print(3)
confere_senha('abcd12!@abcd')  
# inválida

# 4. Sem letra minúscula suficiente
print(4)
confere_senha('ABCD12!@ABCD')  
# inválida

# 5. Sem caracteres especiais
print(5)
confere_senha('Abcd1234Efgh')  
# inválida

# 6. Contém espaço
print(6)
confere_senha('Abc 12!@Efgh')  
# inválida

# 7. Caracteres acentuados como caracteres especiais - DEVE PASSAR
print(7)
confere_senha('Ábcdê123EEff')  
# valida

# 8. Só números e caracteres especiais
print(8)
confere_senha('12!@#$%^&*()')  
# inválida

# 9. Só letras
print(9)
confere_senha('Abcdefghijkl')  
# inválida

# 10. Só maiúsculas e minúsculas
print(10)
confere_senha('AbCdEfGhIjKl')  
# inválida