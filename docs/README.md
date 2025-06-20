# Projeto: Raspagem e Análise do Índice TIOBE

Este projeto realiza a raspagem do ranking de linguagens de programação do índice TIOBE e coleta comentários de programadores sobre as três linguagens mais populares, utilizando agentes autônomos e inteligência artificial.

## Descrição

O software executa duas entregas principais:

1. **Ranking das Linguagens Mais Usadas:**
   - Realiza a raspagem do site do índice TIOBE ([https://www.tiobe.com/tiobe-index/](https://www.tiobe.com/tiobe-index/)) utilizando Python, `requests` e `BeautifulSoup`.
   - Gera uma lista das linguagens de programação mais populares.

2. **Coleta de Comentários de Programadores:**
   - Utiliza uma equipe CrewAI composta por quatro agentes:
     - **Pesquisador:** Busca páginas na internet com comentários sobre as três primeiras linguagens do ranking, usando a API Serper (Google).
     - **Extrator:** Obtém o conteúdo de pelo menos três URLs encontradas, usando `requests` e parsing HTML.
     - **Coletor:** Extrai comentários positivos e negativos dos programadores a partir dos conteúdos, utilizando a API do ChatGPT 4o mini.
     - **Redator:** Resume e organiza os comentários coletados, também usando a API do ChatGPT 4o mini.
   - O resultado é salvo em um arquivo markdown e exibido ao usuário.

## Diagrama Resumido do Pipeline

```
+-------------------+
|   Raspagem TIOBE  |
| (requests + BS4)  |
+---------+---------+
          |
          v
+-------------------+
|   Lista de        |
| Linguagens        |
+---------+---------+
          |
          v
+-------------------+
|   CrewAI Agents   |
+---------+---------+
          |
          v
+-------------------+
| Comentários e     |
| Resumo Final      |
+-------------------+
```

## Instruções de Execução

1. **Clone o repositório:**
   ```powershell
   git clone <url-do-repositorio>
   cd <nome-do-repositorio>
   ```

2. **Crie e ative o ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv_scrap
   .\venv_scrap\Scripts\Activate.ps1
   ```

3. **Instale as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```
   Ou, se estiver usando `pyproject.toml`:
   ```powershell
   pip install uv
   uv sync
   ```

4. **Configure as chaves de API:**
   - Insira suas chaves de API da Serper e do ChatGPT 4o mini nos arquivos de configuração apropriados (verifique a pasta `Comum/LLM/`).

5. **Execute o programa principal:**
   ```powershell
   python scrap/main.py
   ```

6. **Visualize o resultado:**
   - O resultado do scrap é persistido no arquivo `response.html`. 
   - O resultado já limpo e processado é persistido no arquivo markdown `resultado.md`.

## Dependências

- Python 3.12+
- requests
- beautifulsoup4
- openai (para ChatGPT 4o mini)
- Serper API
- Outras dependências podem estar listadas em `requirements.txt` ou `pyproject.toml`.

## Estrutura do Projeto

```
scrap/
  |-- main.py
  |-- ColetagemOpiniaoUsuario.py
  |-- ObtencaoHtml.py
  |-- ObtencaoLinguagem.py
  |-- Work.py
  |-- Comum/
        |-- LLM/
        |-- Models/
        |-- Utils/
  |-- resultado.md
  |-- README.md
venv_scrap/
  |-- ...
```

Citação das Licenças de Datasets ou APIs Utilizadas
O software utiliza diversas bibliotecas e serviços de terceiros, cada um com suas
licenças e termos de uso:

@@@@
## 📊 Dados Coletados

Para cada linguagem de programação, o sistema coleta:

- **Nome da linguagem**
- **Percentual de participação** no índice TIOBE
- **Taxa de crescimento** mensal
- **Opiniões positivas** da comunidade
- **Opiniões negativas** da comunidade
- **Análise consolidada** baseada em múltiplas fontes

## Contribuição

Contribuições são bem-vindas! Por favor:

1. Faça fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Licença de terceiros
- Python: Python Software Foundation License (PSF)
- requests: Apache License
- BeautifulSoup: MIT License
- CrewAI & CrewAI Tools: Geralmente MIT License (veriﬁcar repositórios oﬁciais).
- Serper API (Google Search API): Sujeito aos seus Termos de Serviço.
- ChatGPT  o mini API (OpenAI): Sujeito aos Termos de Uso da OpenAI e Política de Uso.

## Configuração Avançada

### Personalização do Número de Linguagens

No arquivo `main.py`, você pode ajustar a variável `quantidade` para processar mais ou menos linguagens:

```python
quantidade = 2  # Processa as 2 linguagens mais populares
```

### Configuração de Verbosidade

Para logs mais detalhados durante a execução:

```python
work_linguagem = WorkLinguagem(verbose=True)
```

## Observações
- Certifique-se de possuir as chaves de API necessárias.
- O projeto pode ser adaptado para outros rankings ou fontes de comentários.

---

**Desenvolvido com ❤️ para a comunidade de desenvolvedores** 

