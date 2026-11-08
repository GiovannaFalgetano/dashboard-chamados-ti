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
n = 3000

tipo_col = np.random.choice(tipos, size=n)

categoria_col = np.random.choice(categorias, size=n)

prioridade_col = np.random.choice(prioridades, size=n)

status_col = np.random.choice(status, size=n)

departamento_col = np.random.choice(departamentos, size=n)

grupo_col = np.random.choice(grupos, size=n)

df = pd.DataFrame({
    "tipo": tipo_col,
    "categoria": categoria_col,
    "prioridade": prioridade_col,
    "status": status_col,
    "departamento": departamento_col,
    "grupo": grupo_col,
})

print(df.head())
print(df.shape)