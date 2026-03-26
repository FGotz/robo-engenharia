import streamlit as st
import pandas as pd
import base64

# Configuração de Página e Tema
st.set_page_config(page_title="Analista de Orçamentos com IA", page_icon="🏗️", layout="wide", initial_sidebar_state="collapsed")

# CSS para Light Mode, Tipografia e Layout Moderno
st.markdown("""
<style>
/* Forçar Light Mode e Tipografia Sans-serif */
:root {
  --background-color: #ffffff;
  --text-color: #1a202c;
  --primary-color: #003a70; /* Azul Marinho profundo */
  --secondary-color: #f0f4f8; /* Cinza muito claro */
  --font-family: 'Inter', sans-serif;
}

body {
  background-color: var(--background-color);
  color: var(--text-color);
  font-family: var(--font-family);
}

/* Título e Subtítulo */
h1 {
  color: var(--primary-color);
  font-family: var(--font-family);
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

h2, h3, h4 {
  color: var(--primary-color);
  font-family: var(--font-family);
  font-weight: 600;
  margin-top: 2rem;
  margin-bottom: 1rem;
}

p {
  color: #4a5568; /* Cinza médio */
  font-size: 1.1rem;
  line-height: 1.6;
}

/* Área de Upload de Arquivo */
.stFileUpload {
  background-color: var(--secondary-color);
  border: 1px solid #d2dce6;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
}

.stFileUpload > label {
  color: var(--primary-color);
  font-weight: 600;
  font-size: 1.2rem;
}

/* Ícone de Upload */
.stFileUpload::before {
  content: '📤';
  font-size: 3rem;
  display: block;
  text-align: center;
  margin-bottom: 1.5rem;
}

/* Botão de Upload */
.stButton button {
  background-color: var(--primary-color) !important;
  color: #ffffff !important;
  font-family: var(--font-family) !important;
  border-radius: 8px !important;
  padding: 0.75rem 1.5rem !important;
  font-size: 1rem !important;
  font-weight: 600 !important;
}

/* Tabela de Dados */
.dataframe {
  font-family: var(--font-family);
  border-collapse: collapse;
  width: 100%;
}

.dataframe td, .dataframe th {
  border: 1px solid #d2dce6;
  padding: 0.75rem;
}

.dataframe tr:nth-child(even) {
  background-color: #fafbfc;
}

.dataframe th {
  padding-top: 1rem;
  padding-bottom: 1rem;
  text-align: left;
  background-color: #f7fafc;
  color: var(--primary-color);
}

/* Parecer Técnico */
.stAlert {
  background-color: #f1faf1; /* Verde suave de confirmação */
  color: #0d4a0d;
  border-left-color: #2e8b2e;
  border-radius: 8px;
  font-family: var(--font-family);
}

/* Deploy Menu */
.stDeployMenu {
  background-color: #f7fafc;
  color: var(--primary-color);
}
</style>
""", unsafe_allow_html=True)

# Layout
st.title("Analista de Orçamentos com IA")
st.markdown("Faça o upload da sua planilha de insumos (Curva ABC) e receba estratégias automáticas de redução de custos.")

st.subheader("Arraste seu arquivo CSV de orçamento aqui")
uploaded_file = st.file_uploader("Browse files", type="csv")

if uploaded_file is not None:
    # Carregar e processar dados (Simulação)
    df = pd.read_csv(uploaded_file)
    st.success(f"Arquivo '{uploaded_file.name}' carregado com sucesso.")

    st.subheader("Tabela de Insumos (Curva ABC)")
    st.dataframe(df)

    st.subheader("Parecer Técnico da IA")
    # Simulação do relatório da IA
    st.info("""
    **Parecer Técnico de Engenharia**
    * Substituir a alvenaria de vedação (Tijolo Baiano) por bloco estrutural para reduzir o custo em 15%.
    * Implementar controle rigoroso de traço no canteiro de obras para evitar desperdício de cimento.
    * Realizar uma Curva ABC reversa nos itens de acabamento para identificar substitutos mais econômicos.
    """)