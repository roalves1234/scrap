import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.llms import ChatOpenAI

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

class Crew:
    def __init__(self):
        pass 
    
    def get(self, linguagem):
        # Ferramentas
        search_tool = SerperDevTool()
        scraper_tool = ScrapeWebsiteTool()

        # Agente 1: Pesquisador
        pesquisador = Agent(
            role='Pesquisador de Opiniões sobre Linguagens',
            goal='Encontrar críticas e opiniões reais de programadores sobre {linguagem}',
            backstory=(
                "Você é um pesquisador experiente, com foco em entender como as linguagens "
                "de programação são percebidas pela comunidade."
            ),
            verbose=True,
            memory=True,
            tools=[search_tool],
            allow_delegation=True
        )

        # Agente 2: Coletor de Conteúdo
        coletor = Agent(
            role='Coletor de Conteúdo de URLs',
            goal='Extrair conteúdo de leitura de páginas da web',
            backstory=(
                "Você é especialista em extrair conteúdo limpo e legível de páginas web, "
                "removendo tudo que não é relevante para leitura."
            ),
            verbose=True,
            memory=True,
            tools=[scraper_tool],
            allow_delegation=False
        )

        # Agente 3: Redator Resumidor
        redator = Agent(
            role='Redator Técnico',
            goal='Resumir as opiniões encontradas sobre a linguagem {linguagem}',
            backstory=(
                "Você é um redator técnico com talento para sintetizar grandes volumes de informação "
                "em resumos claros, objetivos e bem estruturados."
            ),
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=False,
            llm=ChatOpenAI(model="gpt-4")
        )

        # Tarefa 1: Pesquisa
        pesquisa_task = Task(
            description=(
                "Pesquise no Google por opiniões ou críticas feitas por programadores sobre a linguagem {linguagem}. "
                "Foque em fóruns, artigos de opinião e discussões técnicas com comentários reais de desenvolvedores."
            ),
            expected_output=(
                "Pelo menos 2 URLs com opiniões ou críticas reais de programadores sobre a linguagem {linguagem}."
            ),
            tools=[search_tool],
            agent=pesquisador
        )

        # Tarefa 2: Coleta de conteúdo
        coleta_task = Task(
            description=(
                "Acesse cada uma das URLs fornecidas pela tarefa anterior e colete o conteúdo legível de cada página. "
                "Remova qualquer conteúdo irrelevante como menus, rodapés ou anúncios."
            ),
            expected_output=(
                "Conteúdo limpo e legível de cada URL fornecida, pronto para ser resumido."
            ),
            tools=[scraper_tool],
            agent=coletor
        )

        # Tarefa 3: Resumo
        resumo_task = Task(
            description=(
                "Com base em todos os conteúdos lidos nas tarefas anteriores, escreva um resumo com cerca de 8 linhas. "
                "O resumo deve destacar os principais pontos positivos e negativos mencionados pelos programadores, "
                "bem como qualquer percepção geral sobre a linguagem."
            ),
            expected_output=(
                "Um resumo de aproximadamente 8 linhas cobrindo os temas centrais abordados nos textos."
            ),
            tools=[],
            agent=redator
        )

        # Crew com 3 agentes e tarefas sequenciais
        crew = Crew(
            agents=[pesquisador, coletor, redator],
            tasks=[pesquisa_task, coleta_task, resumo_task],
            process=Process.sequential
        )

        # Execução da crew
        result = crew.kickoff(inputs={"linguagem": linguagem})
        print(result)