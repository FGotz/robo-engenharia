import os
import pandas as pd
from google import genai
from dotenv import load_dotenv

def analisar_orcamento(caminho_arquivo):
    print("🏗️ Iniciando leitura do orçamento da obra...\n")
    
    # 1. Lendo e calculando
    df = pd.read_csv(caminho_arquivo)
    df['Custo_Total'] = df['Quantidade'] * df['Valor_Unitario']
    custo_total_obra = df['Custo_Total'].sum()
    df_ordenado = df.sort_values(by='Custo_Total', ascending=False)
    
    print("📋 TABELA DE CUSTOS ATUALIZADA:")
    print(df_ordenado.to_string(index=False))
    print("-" * 50)
    print(f"💰 CUSTO TOTAL PREVISTO DA OBRA: R$ {custo_total_obra:,.2f}\n")
    
    return df_ordenado, custo_total_obra

def gerar_relatorio_ia(df, custo_total):
    print("🤖 Chamando o Engenheiro de Custos (Gemini)...")
    
    load_dotenv(override=True)
    chave_gemini = os.getenv("GEMINI_API_KEY")
    
    if not chave_gemini:
        print("❌ Erro: Chave do Gemini não encontrada no .env!")
        return
        
    client = genai.Client(api_key=chave_gemini)
    
    # Transformamos a tabela em texto para a IA conseguir ler
    dados_em_texto = df.to_string(index=False)
    
    prompt = f"""
    Aja como um Engenheiro Civil Sênior especialista em orçamentos e suprimentos.
    Aqui está a curva ABC (tabela de insumos) de uma obra, ordenada do item mais caro para o mais barato:
    
    {dados_em_texto}
    
    O custo total previsto da obra é de R$ {custo_total:,.2f}.
    
    Escreva um relatório executivo breve e direto para o Diretor da Construtora:
    1. Aponte quais são os 2 principais "vilões" do orçamento (os itens mais caros).
    2. Dê 2 sugestões práticas de engenharia ou negociação para tentar reduzir o custo DESSES 2 itens específicos sem perder a qualidade estrutural ou de acabamento.
    """
    
    resposta = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
    )
    
    print("\n" + "="*50)
    print("👷 RELATÓRIO DO ENGENHEIRO CHEFE")
    print("="*50)
    print(resposta.text)

if __name__ == "__main__":
    # O código agora faz as duas coisas na sequência
    tabela_pronta, total_calculado = analisar_orcamento("orcamento_obra.csv")
    gerar_relatorio_ia(tabela_pronta, total_calculado)