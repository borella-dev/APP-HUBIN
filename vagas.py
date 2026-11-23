
from arquivos import carregar_dados, salvar_dados

def publicar_vaga(vaga):
    vagas = carregar_dados('vagas.json')
    vagas.append(vaga)
    salvar_dados('vagas.json', vagas)