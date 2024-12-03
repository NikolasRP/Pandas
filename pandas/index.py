# Estrutura do Exercício.
# Passo 1: Carregar e Explorar os Dados.
# Carregar a base de dados chamada "cancelamentos.csv" usando a biblioteca pandas.
# Observar informações gerais da base, identificando valores nulos, colunas e tipos de dados.

import pandas as pd

# Carregar os dados.
df = pd.read_csv('cancelamentos.csv')

# Exibir informações gerais
print(df.info())
print(df.describe())

# Passo 2: Análise Exploratoria para Identificação de Padrões de Cancelamento.
# A análise exploratoria deve focar nos possíveis fatores de cancelamentos.
# Utilizaremos a blibioteca plotly.express para a visualização de dados e para compreender padrões específicos de clientes que cancelaram o serviço.
# Abaixo estão algumas sugestões de análise que podem ser realizadas:
# Distribuição do Tempo como Cliente e Cancelamento: Verificar se clientes ficam menos tempo na empresa são mais propensos a cancelar.

import plotly.express as px

fig = px.histogram(df, x='tempo_como_cliente', color='cancelou', barmode='group', title="Distribuição do Tempo como Cliente")
fig.show()

# Idade vs Cancelamento: Avaliar a idade dos Clientes e a taxa de cancelamento para identificar padrões.

fig = px.histogram(df, x='idade', color='cancelou', barmode='group', title="Distribuição de Idade e Cancelamento")
fig.show()

# Total gasto vs Cancelamento:
# Entender a relação entre o valor gasto pelo cliente e o cancelamento, verificando se há um perfil específico de consumo entre os que cancelaram.

fig = px.histogram(df, x='cancelou', y='total_gasto', title="Distribuição de Total Gasto por Cancelamento")
fig.show()

# Dias de Atraso e Cancelamento: Análisar se clientes que atrasam pagamentos são mais propensos a cancelarar.

fig = px.histogram(df, x='dias_atraso', color='cancelou', barmode='overlay', title="Dias de Atraso e Cancelamento")
fig.show()

# Interações com Call Center e Cancelamento: Observar se o números de ligações para o call center tem relação com o cancelamento.

fig = px.histogram(df, x='cancelou', y='ligacoes_callcenter', title="Número de ligações ao Call Center e Cancelamento")
fig.show()

# Passo 3: Identificação de Perfis e Padrões de Clientes:
# Baseado nas análises anteriores, identifique perfis de clientes com alta probabilidade de cancelar.

# Clientes com alta frequência d atrasos.
# Clientes co menor tempo de permanência.
# Clientes que fazem uso menos frequente do serviço.
# Passo 4: Projeção de Impacto com Ações de Retenção.
# Simule o impacto de mudanças nas taxas de cancelamento ao melhorar fatores específicos, como:

# Redução do número de dias de atrasos.
# Melhoria no atendimento (reduzindo ligações ao call center).
# Aumentar a frequência de uso por meios incentivos.

# Crie uma cópia do dataset e modifique essas variáveis para prever o cenário onde esses fatores são melhorados.

#simulação de cenário onde atrasos e ligações ao call centersão reduzidos para 50% dos valores originais.
df_simulacao = df.copy()
df_simulacao['dias_atraso'] = df_simulacao['dias_atraso'] * 0.5