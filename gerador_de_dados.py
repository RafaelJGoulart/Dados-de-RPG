import json
import os
from itertools import combinations, combinations_with_replacement

# =============================================
# FUNÇÃO 1: Adiciona um dado a uma régua existente
# =============================================
def adicionar_dado(regua, faces_novo_dado):
    """
    Pega a régua atual e adiciona um novo dado.
    
    Args:
        regua: Dicionário {soma: quantidade}
        faces_novo_dado: Número de faces do novo dado
    
    Returns:
        Nova régua com o dado adicionado
    """
    nova_regua = {}
    
    # Para cada soma na régua atual
    for soma_atual, quantidade in regua.items():
        # Para cada face do novo dado
        for face in range(1, faces_novo_dado + 1):
            nova_soma = soma_atual + face
            
            # Adiciona a quantidade na nova soma
            if nova_soma in nova_regua:
                nova_regua[nova_soma] += quantidade
            else:
                nova_regua[nova_soma] = quantidade
    
    return nova_regua


# =============================================
# FUNÇÃO 2: Calcula estatísticas da distribuição
# =============================================
def calcular_estatisticas(distribuicao):
    """
    Calcula estatísticas básicas da distribuição.
    """
    total = sum(distribuicao.values())
    soma_ponderada = sum(soma * qtd for soma, qtd in distribuicao.items())
    media = soma_ponderada / total if total > 0 else 0
    
    return {
        "total_combinacoes": total,
        "media": round(media, 2),
        "min": min(distribuicao.keys()),
        "max": max(distribuicao.keys())
    }


# =============================================
# FUNÇÃO 3: Processa uma combinação específica de dados
# =============================================
def processar_combinacao(lista_dados):
    """
    Processa uma lista de dados e retorna a distribuição final.
    
    Args:
        lista_dados: Lista de números de faces [4, 6, 8, ...]
    
    Returns:
        Dicionário com a distribuição e estatísticas
    """
    # Começa com o primeiro dado
    primeiro = lista_dados[0]
    regua = {face: 1 for face in range(1, primeiro + 1)}
    
    # Adiciona os outros dados um por um
    for faces in lista_dados[1:]:
        regua = adicionar_dado(regua, faces)
    
    # Calcula estatísticas
    estatisticas = calcular_estatisticas(distribuicao=regua)
    
    # Converte chaves para string (para o JSON)
    distribuicao_str = {str(k): v for k, v in regua.items()}
    
    return {
        "distribuicao": distribuicao_str,
        "estatisticas": estatisticas
    }


# =============================================
# FUNÇÃO 4: Gera nome da combinação
# =============================================
def nome_combinacao(lista_dados, quantidades=None):
    """
    Gera um nome para a combinação.
    Se quantidades for None, assume 1 de cada.
    
    Exemplos:
    [4, 6] → "1d4+1d6"
    [4, 4, 4] → "3d4"
    """
    if quantidades is None:
        # Modo antigo: 1 de cada tipo diferente
        return "+".join([f"1d{faces}" for faces in lista_dados])
    else:
        # Modo novo: agrupa por tipo
        from collections import Counter
        contagem = Counter(lista_dados)
        partes = []
        for faces in sorted(contagem.keys()):
            partes.append(f"{contagem[faces]}d{faces}")
        return "+".join(partes)


# =============================================
# FUNÇÃO 5: Gera dados repetidos do mesmo tipo
# =============================================
def gerar_dados_repetidos(faces, quantidade):
    """
    Gera uma lista com 'quantidade' dados do mesmo tipo.
    Exemplo: gerar_dados_repetidos(4, 3) → [4, 4, 4]
    """
    return [faces] * quantidade


# =============================================
# FUNÇÃO 6: Cria estrutura de pastas e salva JSONs
# =============================================
def salvar_resultados(resultados, pasta_base="distribuicoes_dados"):
    """
    Cria pastas e salva os resultados em arquivos JSON.
    
    Estrutura criada:
    distribuicoes_dados/
    ├── 1_dado/
    │   ├── 1d4.json
    │   ├── 2d4.json
    │   ├── 3d4.json
    │   └── ...
    ├── 2_dados/
    │   ├── 1d4+1d6.json
    │   ├── 2d4.json
    │   └── ...
    └── dados_repetidos/
        ├── d4/
        │   ├── 1d4.json
        │   ├── 2d4.json
        │   └── ...
        └── d6/
            └── ...
    """
    # Cria a pasta base
    os.makedirs(pasta_base, exist_ok=True)
    
    for nome, dados in resultados.items():
        # Determina quantos dados tem nessa combinação
        num_dados = nome.count("+") + 1
        
        # Cria a subpasta
        subpasta = os.path.join(pasta_base, f"{num_dados}_dado{'s' if num_dados > 1 else ''}")
        os.makedirs(subpasta, exist_ok=True)
        
        # Caminho do arquivo
        nome_arquivo = os.path.join(subpasta, f"{nome}.json")
        
        # Salva o JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Salvo: {nome_arquivo}")


# =============================================
# FUNÇÃO 7: Salva dados repetidos em pastas separadas
# =============================================
def salvar_dados_repetidos(resultados_repetidos, pasta_base="distribuicoes_dados"):
    """
    Salva os dados repetidos em uma estrutura de pastas organizada por tipo de dado.
    """
    pasta_repetidos = os.path.join(pasta_base, "dados_repetidos")
    os.makedirs(pasta_repetidos, exist_ok=True)
    
    for nome, dados in resultados_repetidos.items():
        # Extrai o tipo de dado (ex: "2d4" → "d4")
        tipo_dado = nome.split('d')[1]
        
        # Cria subpasta para o tipo de dado
        subpasta = os.path.join(pasta_repetidos, f"d{tipo_dado}")
        os.makedirs(subpasta, exist_ok=True)
        
        # Caminho do arquivo
        nome_arquivo = os.path.join(subpasta, f"{nome}.json")
        
        # Salva o JSON
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Salvo (repetido): {nome_arquivo}")


# =============================================
# FUNÇÃO PRINCIPAL
# =============================================
def main():
    """
    Função principal que gera todas as combinações e salva os resultados.
    """
    # Dados disponíveis
    dados_disponiveis = [4, 6, 8, 10, 12, 20]
    
    # Dicionários para guardar os resultados
    todos_resultados = {}
    resultados_repetidos = {}
    
    print("🎲 Gerando combinações de dados...")
    print("=" * 60)
    
    # =============================================
    # PARTE 1: Combinações de dados DIFERENTES
    # =============================================
    print("\n📊 PARTE 1: Dados diferentes (1 de cada tipo)")
    print("-" * 40)
    
    for tamanho in range(1, len(dados_disponiveis) + 1):
        print(f"\n🔄 Processando {tamanho} dado(s) diferentes...")
        
        for combo in combinations(dados_disponiveis, tamanho):
            lista_dados = list(combo)
            nome = nome_combinacao(lista_dados)
            
            # Processa a combinação
            resultado = processar_combinacao(lista_dados)
            todos_resultados[nome] = resultado
            
            # Mostra um resuminho
            total = resultado["estatisticas"]["total_combinacoes"]
            media = resultado["estatisticas"]["media"]
            print(f"   ✅ {nome}: {total:,} combinações, média {media}")
    
    # =============================================
    # PARTE 2: Dados REPETIDOS do mesmo tipo
    # =============================================
    print("\n" + "=" * 60)
    print("📊 PARTE 2: Dados repetidos (2d4, 3d4, ..., 10d4, etc.)")
    print("-" * 40)
    
    for faces in dados_disponiveis:
        print(f"\n🎲 Processando d{faces}...")
        
        for quantidade in range(1, 11):  # 1 até 10 dados
            lista_dados = gerar_dados_repetidos(faces, quantidade)
            nome = f"{quantidade}d{faces}"
            
            # Processa a combinação
            resultado = processar_combinacao(lista_dados)
            resultados_repetidos[nome] = resultado
            
            # Também adiciona aos resultados gerais
            todos_resultados[nome] = resultado
            
            # Mostra um resuminho
            total = resultado["estatisticas"]["total_combinacoes"]
            media = resultado["estatisticas"]["media"]
            print(f"   ✅ {nome}: {total:,} combinações, média {media}")
    
    # =============================================
    # PARTE 3: Salvar tudo
    # =============================================
    print("\n" + "=" * 60)
    print("💾 Salvando arquivos...")
    print("-" * 40)
    
    # Salva os resultados de dados diferentes
    salvar_resultados(todos_resultados)
    
    # Salva os dados repetidos em pastas organizadas
    salvar_dados_repetidos(resultados_repetidos)
    
    # Também salva um arquivo com todas as combinações juntas
    with open("todas_combinacoes.json", 'w', encoding='utf-8') as f:
        json.dump(todos_resultados, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Arquivo completo salvo: todas_combinacoes.json")
    print(f"\n📁 Total de combinações processadas:")
    print(f"   • Dados diferentes: {len(todos_resultados) - len(resultados_repetidos)}")
    print(f"   • Dados repetidos: {len(resultados_repetidos)}")
    print(f"   • TOTAL GERAL: {len(todos_resultados)}")


# =============================================
# EXECUTA O PROGRAMA
# =============================================
if __name__ == "__main__":
    main()