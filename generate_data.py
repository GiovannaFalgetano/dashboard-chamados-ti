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

min_horas = {"Alta": 2, "Média": 8, "Baixa": 12}
max_horas = {"Alta": 6, "Média": 80, "Baixa": 140}

np.random.seed(42)
n = 3000

tipo_col = np.random.choice(tipos, size=n)

categoria_col = np.random.choice(categorias, size=n)

prioridade_col = np.random.choice(prioridades, size=n)

status_col = np.random.choice(status, size=n)

departamento_col = np.random.choice(departamentos, size=n)

grupo_col = np.random.choice(grupos, size=n)

inicio = pd.Timestamp("2026-05-01")
dias = np.random.randint(0, 180, size=n)
horas = np.random.randint(8, 18, size=n)

abertura_col = inicio + pd.to_timedelta(dias, unit="D") + pd.to_timedelta(horas, unit="h")

prazo_col = pd.Series(prioridade_col).map(sla_horas)

minimos = pd.Series(prioridade_col).map(min_horas).to_numpy()
maximos = pd.Series(prioridade_col).map(max_horas).to_numpy()

horas_resolucao_col = np.random.randint(minimos, maximos)

sla_cumprido_col = horas_resolucao_col <= prazo_col

df = pd.DataFrame({
    "tipo": tipo_col,
    "categoria": categoria_col,
    "prioridade": prioridade_col,
    "status": status_col,
    "departamento": departamento_col,
    "grupo": grupo_col,
    "aberto_em": abertura_col,
    "prazo_sla": prazo_col,
    "horas_resolucao": horas_resolucao_col,
    "sla_cumprido": sla_cumprido_col,
})

print(df.head())
print(df["aberto_em"].min(), df["aberto_em"].max())
print(df["sla_cumprido"].mean())