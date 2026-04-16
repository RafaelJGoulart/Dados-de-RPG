
![Versão](https://img.shields.io/badge/versão-1.0.0-7b3fe4?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow?style=flat-square&logo=javascript)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3)
![Licença](https://img.shields.io/badge/Licença-MIT-7b3fe4?style=flat-square)

---

## 📖 Sobre o Projeto

O **Nexus Dice** é uma ferramenta completa para análise de distribuições de probabilidade em jogos de RPG de mesa. O sistema calcula matematicamente todas as combinações possíveis de dados (d4, d6, d8, d10, d12, d20), gerando distribuições exatas sem necessidade de simulações ou força bruta computacional.

### ✨ Principais Características

- ✅ **Cálculo exato de probabilidades** usando convolução de distribuições discretas
- ✅ **Geração de combinações** com 1 até 6 dados diferentes (sem repetição)
- ✅ **Suporte a dados repetidos** (2d4, 3d6, até 10 dados do mesmo tipo)
- ✅ **Exportação em JSON** estruturado por pastas organizadas
- ✅ **Visualização interativa** com gráficos dinâmicos em HTML/CSS/JS
- ✅ **Interface moderna** com tema roxo, glassmorphism e design responsivo
- ✅ **Estatísticas completas** para cada combinação (total, média, min, max)

---

## 🧮 O Algoritmo de Convolução

O coração do projeto utiliza **convolução de distribuições discretas** para calcular as probabilidades. Em vez de gerar cada combinação individual (abordagem de força bruta), o algoritmo:

1. Representa cada dado como uma distribuição de frequências (ex: d4 = `{1:1, 2:1, 3:1, 4:1}`)
2. Convolui sequencialmente as distribuições, combinando as probabilidades
3. Acumula as contagens matematicamente, sem enumerar combinações

Esta abordagem reduz drasticamente a complexidade computacional:

| Método | Complexidade | Exemplo (6 dados) |
|--------|--------------|-------------------|
| Força Bruta | O(∏ faces) | ~4.6 milhões de operações |
| **Convolução** | **O(d × m)** | **~1.500 operações** |

Onde `d` é o número de dados e `m` o tamanho da distribuição resultante.

### Exemplo Didático: 1d4 + 1d6

` ` `
Distribuição d4: {1:1, 2:1, 3:1, 4:1}
Distribuição d6: {1:1, 2:1, 3:1, 4:1, 5:1, 6:1}

Convolução (d4 + d6):
- Soma 2: 1+1 = 1 maneira
- Soma 3: 1+2, 2+1 = 2 maneiras
- Soma 4: 1+3, 2+2, 3+1 = 3 maneiras
...
Resultado: {2:1, 3:2, 4:3, 5:4, 6:4, 7:4, 8:3, 9:2, 10:1}
` ` `

---

## 📁 Estrutura do Projeto

` ` `
nexus-dice/
│
├── 📄 gerar_distribuicoes.py      # Script Python que gera todas as combinações
├── 📄 visualizador.html            # Interface web para visualização dos dados
├── 📄 README.md                    # Este arquivo
│
├── 📁 distribuicoes_dados/         # Pasta com os JSONs gerados (organizados)
│   ├── 📁 1_dado/
│   │   ├── 1d4.json
│   │   ├── 1d6.json
│   │   └── ...
│   ├── 📁 2_dados/
│   │   ├── 1d4+1d6.json
│   │   └── ...
│   ├── 📁 3_dados/
│   ├── 📁 4_dados/
│   ├── 📁 5_dados/
│   ├── 📁 6_dados/
│   └── 📁 dados_repetidos/
│       ├── 📁 d4/
│       │   ├── 2d4.json
│       │   ├── 3d4.json
│       │   └── ...
│       ├── 📁 d6/
│       └── ...
│
└── 📄 todas_combinacoes.json       # Arquivo único consolidado com todos os resultados
` ` `

---

## 🚀 Como Usar

### 📥 Pré-requisitos

- Python 3.8 ou superior instalado
- Navegador web moderno (Chrome, Firefox, Edge, Safari)
- Nenhuma biblioteca externa necessária (apenas bibliotecas padrão do Python)

### Gerando os Dados

Execute o script Python para gerar todas as distribuições:

` ` `bash
python gerar_distribuicoes.py
` ` `

**O que acontece:**
- O script calcula 123 combinações diferentes (63 com dados diferentes + 60 com dados repetidos)
- Cria a estrutura de pastas automaticamente
- Gera arquivos JSON individuais e um arquivo consolidado
- Exibe o progresso no terminal

**Tempo estimado:** Menos de 2 segundos para todas as combinações!

### Visualizando os Gráficos

1. Abra o arquivo `visualizador.html` no seu navegador (duplo clique)
2. Clique em "Selecionar Arquivo JSON" e escolha o arquivo `todas_combinacoes.json`
3. Explore os gráficos usando:
   - 🔍 Barra de busca para filtrar por nome
   - 🎛️ Botões de filtro por quantidade de dados
   - 📊 Hover nos gráficos para ver porcentagens detalhadas

---

## Exemplos de Saída

### JSON gerado para `1d4+1d6.json`:

` ` `json
{
  "distribuicao": {
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 4,
    "7": 4,
    "8": 3,
    "9": 2,
    "10": 1
  },
  "estatisticas": {
    "total_combinacoes": 24,
    "media": 6.0,
    "min": 2,
    "max": 10
  }
}
` ` `

### JSON gerado para `3d4.json`:

` ` `json
{
  "distribuicao": {
    "3": 1,
    "4": 3,
    "5": 6,
    "6": 10,
    "7": 12,
    "8": 12,
    "9": 10,
    "10": 6,
    "11": 3,
    "12": 1
  },
  "estatisticas": {
    "total_combinacoes": 64,
    "media": 7.5,
    "min": 3,
    "max": 12
  }
}
` ` `

---

## Combinações Suportadas

### Dados Diferentes (sem repetição)
São geradas **63 combinações** usando combinações únicas dos dados disponíveis:

| Quantidade | Exemplos | Total |
|------------|----------|-------|
| 1 dado | 1d4, 1d6, 1d8, 1d10, 1d12, 1d20 | 6 |
| 2 dados | 1d4+1d6, 1d4+1d8, ..., 1d12+1d20 | 15 |
| 3 dados | 1d4+1d6+1d8, 1d4+1d6+1d10, ... | 20 |
| 4 dados | ... | 15 |
| 5 dados | ... | 6 |
| 6 dados | 1d4+1d6+1d8+1d10+1d12+1d20 | 1 |

### Dados Repetidos (do mesmo tipo)
São geradas **60 combinações** adicionais:

| Tipo | Quantidades |
|------|-------------|
| d4 | 2d4, 3d4, 4d4, 5d4, 6d4, 7d4, 8d4, 9d4, 10d4 |
| d6 | 2d6, 3d6, ..., 10d6 |
| d8 | 2d8, 3d8, ..., 10d8 |
| d10 | 2d10, 3d10, ..., 10d10 |
| d12 | 2d12, 3d12, ..., 10d12 |
| d20 | 2d20, 3d20, ..., 10d20 |

**Total geral: 123 combinações processadas!**

---

## Tecnologias Utilizadas

### Backend (Geração de Dados)
- **Python 3.8+** - Linguagem principal
- **itertools.combinations** - Geração de combinações únicas
- **json** - Serialização e exportação estruturada
- **os / os.path** - Gerenciamento de sistema de arquivos

### Frontend (Visualização)
- **HTML5** - Estrutura semântica e acessível
- **CSS3** - Estilização moderna com:
  - Flexbox e Grid Layout
  - Glassmorphism (backdrop-filter)
  - Gradientes e animações suaves
  - Design responsivo (mobile-first)
- **JavaScript (ES6+)** - Lógica de renderização e interatividade
- **Chart.js 3.x** - Biblioteca de gráficos de barras

---

## Performance e Otimizações

### Comparação de Desempenho

| Combinação | Força Bruta | Convolução | Melhoria |
|------------|-------------|------------|----------|
| 1d4+1d6 | 24 ops | 24 ops | 1x |
| 3d4 | 64 ops | 16 ops | 4x |
| 1d4+1d6+1d8 | 192 ops | 72 ops | 2.6x |
| 6 dados diferentes | 4.608.000 ops | ~1.518 ops | **~3.000x** |
| 10d4 | 1.048.576 ops | ~100 ops | **~10.000x** |

### Otimizações Implementadas

- **Algoritmo de convolução** - Evita geração de combinações individuais
- **Dicionários esparsos** - Armazena apenas posições com valores > 0
- **Debounce na busca** - Aguarda 250ms antes de re-renderizar
- **RequestAnimationFrame** - Inicialização não-bloqueante dos gráficos
- **Limpeza de memória** - Gráficos antigos são destruídos antes de novos

---

## Interface do Visualizador

O visualizador HTML oferece uma experiência completa:

### Funcionalidades
- **Busca em tempo real** - Filtra combinações pelo nome
- **Filtros por quantidade** - Visualize apenas 1 dado, 2 dados, etc.
- **Gráficos interativos** - Hover revela valores exatos e porcentagens
- **Estatísticas consolidadas** - Total de combinações, média, máximo
- **Tema roxo moderno** - Design imersivo com glassmorphism
- **Totalmente responsivo** - Funciona em desktop, tablet e mobile

### Elementos Visuais
- Grid futurista no background
- Cards com efeito de vidro fosco (backdrop blur)
- Gradientes em tons de roxo e azul
- Animações suaves de hover
- Scrollbar estilizada

---

## Notas de Desenvolvimento

Este projeto foi concebido como um estudo aprofundado sobre:

- **Matemática discreta** aplicada a jogos de RPG
- **Algoritmos de convolução** para distribuições de probabilidade
- **Otimização computacional** em problemas combinatórios
- **Visualização de dados** probabilísticos de forma intuitiva
- **Estruturação de dados** para exportação e consumo

Durante o desenvolvimento, foram exploradas diferentes abordagens matemáticas e computacionais. O algoritmo de convolução, em particular, revelou-se uma solução elegante e extremamente eficiente para o problema, transformando uma complexidade exponencial em linear.

A implementação priorizou:
1. **Clareza de código** - Funções bem definidas e comentadas
2. **Modularidade** - Separação entre geração e visualização
3. **Performance** - Uso de estruturas de dados adequadas
4. **Usabilidade** - Interface intuitiva e responsiva

---

## Possíveis Extensões

Ideias para futuras melhorias:

- [ ] Suporte a **modificadores** (ex: 1d6+2, 2d8+5)
- [ ] Cálculo de **probabilidade condicional** (ex: "chance de tirar ≥ 15")
- [ ] **Comparação lado a lado** de diferentes combinações
- [ ] Exportação para **CSV** e **Excel**
- [ ] **Modo escuro/claro** no visualizador
- [ ] **Gráficos de linha** para visualizar a curva de distribuição
- [ ] **Download em lote** de todos os JSONs em ZIP
- [ ] Suporte a **dados não-justos** (probabilidades personalizadas)

---

## Licença

Este projeto está licenciado sob a **MIT License** - sinta-se livre para usar, modificar e distribuir como desejar.

` ` `
MIT License

Copyright (c) 2024 Nexus Dice

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
` ` `

---

## 🙏 Agradecimentos

- À comunidade de RPG, por inspirar a exploração matemática dos jogos
- Aos desenvolvedores de bibliotecas open-source que tornaram este projeto possível
- A todos que contribuem para a democratização do conhecimento em programação e matemática

---

<p align="center">
  <br>
  <i>Desenvolvido com 💜 para mestres e jogadores de RPG</i>
  <br><br>
  <sub>
    ✨ "A matemática é a verdadeira mágica por trás de cada rolagem de dado" ✨
  </sub>
  <br><br>
  <img src="https://img.shields.io/badge/Made%20with-Passion-7b3fe4?style=for-the-badge">
</p>

