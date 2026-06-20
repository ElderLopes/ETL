import pandas as pd


print("Iniciando a Extração dos dados...")

df_usuarios = pd.read_csv('usuarios.csv')
print(df_usuarios)
print("-" * 40)


print("Iniciando a Transformação...")

def gerar_mensagem_marketing(nome):
    return f"Olá {nome}! Já pensou em proteger o seu patrimônio hoje? Conheça nossos novos CDBs."

df_usuarios['Mensagem_Marketing'] = df_usuarios['Nome'].apply(gerar_mensagem_marketing)

print("Dados transformados com as novas mensagens:")
print(df_usuarios[['Nome', 'Mensagem_Marketing']])
print("-" * 40)

print("Iniciando o Carregamento (Salvando os dados)...")

nome_arquivo_saida = 'usuarios_transformados.csv'
df_usuarios.to_csv(nome_arquivo_saida, index=False)

print(f"Processo concluído com sucesso! Verifique o arquivo: {nome_arquivo_saida}")