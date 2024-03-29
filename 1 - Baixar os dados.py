import pandas as pd


url1 = 'cole a url aqui'
url2 = 'cole a url aqui'


df1 = pd.read_excel(url1, sheet_name='0.3. Menu')
df2 = pd.read_excel(url2, sheet_name=None)

df1 = df1.dropna(how='all')

df1 = df1.rename(columns={
    'P_0.1': 'IDENTIFICAÇÃO DO(A) PESQUISADOR(A)',
    'P_0.2': 'IDENTIFICADOR DO DOMICÍLIO',
    'P_0.3': 'VERIFICADOR DOMICÍLIO',
    'P_0.4': 'TRECHO DA RUA DO DOMICÍLIO TEM PAVIMENTAÇÃO?',
    'P_0.5': 'TRECHO DA RUA DO DOMICÍLIO TEM CALÇADA?',
    'P_0.5.1': 'QUAL A CONDIÇÃO DA CALÇADA?',
    'P_0.6': 'RESULTADO PRELIMINAR DA PESQUISA',
    'P_0.7': 'TELEFONE DO(A) MORADOR(A) PARA CONTATO',
    'P_0.8': 'COMENTÁRIOS',

})

caminho_arquivo_saida = r'mude para diretório de sua escolha e adicione a extensão excel.xlsx'

with pd.ExcelWriter(caminho_arquivo_saida, engine='xlsxwriter') as writer:
    df1.to_excel(writer, sheet_name='MENU', index=False)


    for aba, df_aba in df2.items():
        df_aba = df_aba.dropna(how='all')
        df_aba.to_excel(writer, sheet_name=aba, index=False)
