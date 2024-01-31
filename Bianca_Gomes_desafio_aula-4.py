# %%
pip install plyer

# %%
from plyer import notification
from datetime import datetime


def alerta(nivel, base, etapa):
    niveis = {1: 'Alerta Baixo', 2: 'Alerta Médio', 3: 'Alerta Alto'}
    titulo = niveis.get(nivel, 'Nível Invalido')
    data_atual = datetime.now().strftime ("%d-%m-%Y %H:%M:%S")
    mensagem = f'Falha no carregamento da base {base} na etapa {etapa}'
   
    notification.notify(
        title=titulo,
        message=mensagem,
        app_name='Alerta de Falha',
        timeout=10 
    )

print (alerta(1, "A", "1"))


