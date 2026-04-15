# 📦 Sistema de Gestão de Peças e Controle de Qualidade Industrial

## 📖 Sobre o Projeto

Este projeto consiste no desenvolvimento de um sistema completo em **Python** com banco de dados **SQLite**, voltado para a simulação de um processo de controle de qualidade em uma linha de produção industrial.

A proposta central é substituir processos manuais por uma solução automatizada capaz de validar, classificar, organizar e monitorar peças produzidas, garantindo maior eficiência, padronização e confiabilidade dos dados.

O sistema foi desenvolvido com foco educacional, mas segue conceitos aplicáveis a cenários reais da indústria, incluindo automação de processos, validação de dados e organização estruturada da produção.

---

## 🎯 Objetivos do Sistema

O sistema tem como principais objetivos:

- Automatizar o processo de inspeção de qualidade de peças
- Reduzir erros humanos no processo de validação
- Organizar automaticamente as peças em caixas
- Controlar o fluxo de produção
- Disponibilizar relatórios para análise de desempenho

---

## 🚀 Funcionalidades

O sistema possui diversas funcionalidades que simulam um ambiente industrial real:

### 🔹 Cadastro de Peças
Permite inserir novas peças no sistema com informações como:
- ID
- Peso
- Cor
- Comprimento

---

### 🔹 Validação Automática
Cada peça é automaticamente analisada com base em critérios definidos:

- Peso dentro do padrão
- Cor permitida
- Comprimento adequado

O sistema retorna:
- ✅ **Aprovada**
- ❌ **Reprovada (com motivo detalhado)**

---

### 🔹 Classificação Inteligente
As peças são automaticamente classificadas como:
- Aprovadas (armazenadas em caixas)
- Reprovadas (registradas com erro)

---

### 🔹 Organização em Caixas
- Apenas peças aprovadas são armazenadas
- Cada caixa suporta até **10 peças**
- Quando o limite é atingido:
  - A caixa é automaticamente fechada
  - Uma nova caixa é criada

---

### 🔹 Listagem de Peças
Permite visualizar:

- Peças aprovadas
- Peças reprovadas

Com detalhes completos:
- ID
- Peso
- Cor
- Comprimento
- Status

---

### 🔹 Remoção de Peças
Permite excluir peças do sistema pelo ID.

---

### 🔹 Gestão de Caixas
Exibe todas as caixas com:

- ID da caixa
- Status (aberta ou fechada)
- Quantidade de peças armazenadas

---

### 🔹 Relatório de Produção
Gera um resumo completo contendo:

- Total de peças cadastradas
- Quantidade de peças aprovadas
- Quantidade de peças reprovadas
- Número de caixas abertas
- Número de caixas fechadas

---

## 🧠 Regras de Negócio

Uma peça será considerada **APROVADA** somente se atender aos seguintes critérios:

- Peso entre **95g e 105g**
- Cor: **azul** ou **verde**
- Comprimento entre **10cm e 20cm**

Caso qualquer condição não seja atendida, a peça será considerada **REPROVADA**, sendo exibida a justificativa.

---

## 🗃️ Estrutura do Banco de Dados

O sistema utiliza um banco de dados local SQLite com duas tabelas principais:

### 📦 Tabela: `caixas`

| Campo         | Tipo    | Descrição                  |
|--------------|--------|---------------------------|
| id           | INTEGER | Identificador da caixa    |
| status_caixa | TEXT    | aberta ou fechada         |

---

### 🔩 Tabela: `pecas`

| Campo        | Tipo    | Descrição                        |
|-------------|--------|---------------------------------|
| id_peca     | INTEGER | Identificador da peça           |
| peso        | REAL    | Peso da peça                    |
| cor         | TEXT    | Cor da peça                     |
| comprimento | REAL    | Comprimento da peça             |
| aprovada    | INTEGER | 1 = aprovada / 0 = reprovada    |
| status      | TEXT    | Descrição do resultado          |
| caixa_id    | INTEGER | Caixa associada (se aprovada)   |

---

## ⚙️ Arquitetura do Sistema

O sistema foi estruturado de forma modular, com funções específicas para cada responsabilidade:

- `criar_banco()` → Criação do banco e tabelas
- `validar_peca()` → Regras de validação
- `cadastrar_peca()` → Inserção e lógica de caixas
- `listar_pecas()` → Consulta com filtros
- `remover_peca()` → Exclusão de registros
- `listar_caixas()` → Visualização das caixas
- `relatorio()` → Geração de métricas
- `app()` → Menu principal (loop do sistema)

Essa separação facilita manutenção, escalabilidade e organização do código.

---


### 🔹 1. Clone o repositório

```bash
git clone https://github.com/bohrluc/sistema-de-gest-o-de-pe-as-/edit/main/README.md
