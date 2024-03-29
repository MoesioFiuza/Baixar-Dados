import pandas as pd

planilha = r'C:\Users\maest\OneDrive\Área de Trabalho\tratamento\tratamentoResultado_Final.xlsx'
df_deslocamento = pd.read_excel(planilha, sheet_name='3. Deslocamento')
df_menu = pd.read_excel(planilha, sheet_name='MENU')
df_morador = pd.read_excel(planilha, sheet_name='2. Morador')
df_domicilio = pd.read_excel(planilha, sheet_name='1. Dados do Domicílio')
df_transporte = pd.read_excel(planilha, sheet_name='3.8 Meio de Transporte declarad')
df_entrega = pd.read_excel(planilha, sheet_name='3.14 Informações de Entregas')
df_serviço = pd.read_excel(planilha, sheet_name='3.15 Informações de Serviços')
df_moto = pd.read_excel(planilha, sheet_name='1.20 Motocicleta')
df_carro = pd.read_excel(planilha, sheet_name='1.21. Carro')



df_deslocamento['ORIGEM_FORMATADA'] = ''
df_deslocamento['DESTINO_FORMATADO'] = ''
df_menu['ZONA'] = ''
df_menu['VALIDAÇÃO'] = ''
df_menu['GEOCODIFICADO'] = ''
df_domicilio['VALIDAÇÃO'] = ''
df_morador['VALIDAÇÃO'] = ''
df_deslocamento['VALIDAÇÃO'] = ''
df_deslocamento['ORIGEM GEOCODIFICADA'] = ''
df_deslocamento['DESTINO GEOCODIFICADO'] = ''
df_morador['VALIDAÇÃO'] = ''


with pd.ExcelWriter(planilha, engine='xlsxwriter') as writer:
    df_menu.to_excel(writer, sheet_name='MENU', index=False)
    df_domicilio.to_excel(writer, sheet_name='1. Dados do Domicílio', index=False)
    df_morador.to_excel(writer, sheet_name='2. Morador', index=False)
    df_deslocamento.to_excel(writer, sheet_name='3. Deslocamento', index=False)
    df_moto.to_excel(writer, sheet_name='1.20 Motocicleta', index=False)
    df_carro.to_excel(writer, sheet_name='1.21. Carro', index=False)
    df_entrega.to_excel(writer, sheet_name='3.14 Informações de Entregas', index=False)
    df_serviço.to_excel(writer, sheet_name='3.15 Informações de Serviços', index=False)
    df_transporte.to_excel(writer, sheet_name='3.8 Meio de Transporte declarad', index=False)
    df_deslocamento.to_excel(writer, sheet_name='3. Deslocamento', index=False)
