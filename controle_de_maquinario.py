cargo ='supervior'
hora_atual= 4
chave_emergencia= False

# regras de acesso
if ( chave_emergencia == 'true' or cargo
    == 'supervisor'or 'operador' and 8 <= hora_atual <=17): 
    print ('acesso aprovado')
else:
    print('acesso bloqueado')