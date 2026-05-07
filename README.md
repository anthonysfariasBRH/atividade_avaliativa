# Teste Técnico. Desenvolvedor Júnior

## Objetivo

Avaliar sua capacidade de entender um projeto simples com backend e frontend, identificar um problema na lógica, corrigir a implementação e garantir que os testes passem.

O sistema é uma pequena aplicação de **cálculo de desconto**: o usuário informa um preço original e uma porcentagem de desconto, e a aplicação retorna o preço final.

---

## Estrutura do projeto

```
teste_avaliativo_Christian/
├── backend/              # API em Python (FastAPI)
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py       # Inicialização da API e CORS
│   │   └── discount.py   # Lógica de cálculo (contém o problema)
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_discount.py  # Testes automatizados (pytest)
│   ├── requirements.txt
│   └── pytest.ini
├── frontend/             # Interface em ReactJS (Vite)
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
└── README.md
```

---

## Pré-requisitos

- Python 3.10 ou superior
- Node.js 18 ou superior
- npm (vem junto com o Node.js)

---

## Instruções para o candidato

1. Clone ou baixe este projeto.
2. Instale as dependências do **backend** (ver seção abaixo).
3. Execute os **testes do backend** e observe o resultado.
4. Rode o **backend** localmente.
5. Instale as dependências do **frontend**.
6. Rode o **frontend** localmente.
7. Abra a aplicação no navegador e teste alguns cenários.
8. Identifique **por que algum teste está falhando** ou **por que o resultado exibido na tela parece estranho**.
9. Corrija o código do **backend**.
10. **Não altere os testes**, a menos que encontre um erro claro neles (justifique no commit/entrega caso o faça).
11. Após corrigir a falha principal, crie uma integração no **backend** para registrar os cálculos realizados.
12. Essa integração deve salvar os dados em uma **planilha Excel**.
13. Para cada cálculo realizado, salve pelo menos:
    - preço original;
    - percentual de desconto;
    - preço final calculado;
    - data e hora da operação.
14. A planilha pode ser criada automaticamente pelo backend caso ainda não exista.
15. O candidato pode escolher a biblioteca Python para gerar ou atualizar a planilha, como `openpyxl`, `pandas` ou outra equivalente.
16. Limpe e organize todo o código (atualmente GO Horse).
17. Ao finalizar, envie o projeto corrigido (zip ou link do repositório).

    ## Desafio extra obrigatório

Depois de corrigir a falha no cálculo, implemente no backend uma funcionalidade para registrar cada cálculo realizado em uma planilha Excel.

A cada chamada bem-sucedida do endpoint de cálculo, o backend deve salvar uma nova linha na planilha contendo os dados da operação.

A solução deve ser simples, mas funcional. O objetivo é avaliar se o candidato consegue estender uma API existente, lidar com persistência básica de dados e manter o código organizado.

---

## Backend — como rodar

A partir da raiz do projeto:

```bash
cd backend
python -m venv venv
source venv/bin/activate          # Linux/Mac
# venv\Scripts\activate           # Windows (PowerShell/CMD)
pip install -r requirements.txt
```

### Rodar os testes

```bash
pytest
```

### Subir a API

```bash
uvicorn app.main:app --reload
```

A API ficará disponível em `http://localhost:8000`.

Documentação interativa: `http://localhost:8000/docs`.

### Endpoint disponível

`POST /discount`

Entrada (JSON):

```json
{
  "price": 100,
  "discount": 10
}
```

Saída esperada (JSON):

```json
{
  "final_price": 90
}
```

### Regras de negócio esperadas

- O preço original (`price`) deve ser **maior que zero**.
- O desconto (`discount`) deve estar **entre 0 e 100** (inclusive).
- O resultado deve ser o **preço final** após aplicar o desconto percentual.
- Se os valores forem inválidos, a API deve retornar uma resposta de erro adequada (HTTP 400).

---

## Frontend — como rodar

Em outro terminal, a partir da raiz do projeto:

```bash
cd frontend
npm install
npm run dev
```

A interface ficará disponível em `http://localhost:5173`.

> **Atenção:** o frontend faz requisições para `http://localhost:8000`. Mantenha o backend rodando em paralelo.

---

## O que será avaliado

Você **não precisa criar nada complexo**. O foco é:

- **Entendimento do problema:** ler o código existente e descobrir o que está errado.
- **Correção da lógica no backend:** ajustar a implementação para que os testes passem e o resultado fique coerente com as regras descritas.
- **Integração frontend/backend:** confirmar que a tela exibe o resultado correto após a correção.
- **Tratamento básico de erros:** garantir que entradas inválidas sejam rejeitadas e exibidas adequadamente.
- **Testes passando:** todos os testes em `backend/tests/` devem estar verdes ao final.
- **Simplicidade e organização:** mantenha o código limpo, sem mudanças desnecessárias.
- **Clareza da solução:** se quiser, escreva um pequeno parágrafo de entrega explicando o que você identificou e corrigiu.

### Critérios de avaliação

| Critério | Peso |
|---|---|
| Identificou o bug corretamente | Alto |
| Correção mínima e bem direcionada | Alto |
| Testes passando ao final | Alto |
| Frontend integrado e funcional | Médio |
| Tratamento de erros visível na UI | Médio |
| Organização e clareza do código | Médio |

---

## Dicas

- Comece rodando `pytest`. A saída dele já indica em que cenário a lógica falha.
- Compare manualmente o que a API retorna com o que **deveria** retornar segundo as regras descritas acima.
- Não é preciso reescrever a aplicação, geralmente o ajuste é em **poucas linhas**.

Boa prova!
