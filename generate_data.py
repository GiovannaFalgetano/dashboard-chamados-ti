import pandas as pd
import numpy as np

tipos = ["Incidente", "Requisição"]
categorias = ["Hardware", "Software", "Rede", "Segurança"]
prioridades = ["Baixa", "Média", "Alta"]
status = ["Aberto", "Em andamento", "Aguardando usuário", "Resolvido", "Cancelado"]
departamentos = [
    "Produção",
    "Logística",
    "Qualidade",
    "RH",
    "Financeiro",
    "Manutenção",
    "Administrativo",
    "Engenharia",
]
grupos = ["Suporte N1", "Suporte N2", "Infraestrutura"]
sla_horas = {
    "Baixa": 120,
    "Média": 72,
    "Alta": 24,
}

np.random.seed(42)

tipo_col = np.random.choice(tipos, size=10)
print(tipo_col)

categoria_col = np.random.choice(categorias, size=10)
print(categoria_col)

prioridade_col = np.random.choice(prioridades, size=10)
print(prioridade_col)

status_col = np.random.choice(status, size=10)
print(status_col)

departamento_col = np.random.choice(departamentos, size=10)
print(departamento_col)

grupo_col = np.random.choice(grupos, size=10)
print(grupo_col)