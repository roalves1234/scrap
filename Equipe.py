print("Carregamento das bibliotecas")
import os
from crewai import LLM, Agent, Task, Crew, Process
from crewai_tools import SerperDevTool, ScrapeWebsiteTool

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

class Equipe:
    def __init__(self):
        pass 
    
    def get(self, linguagem):
       
        ### FERRAMENTAS ###
        search_tool = SerperDevTool()
        scraper_tool = ScrapeWebsiteTool()
        llm_4o_mini = LLM(model="openai/gpt-4o-mini")


        ### O PESQUISADOR ###
        pesquisador = Agent(
            role='Pesquisador de críticas ou opiniões sobre Linguagens',
            goal='Encontrar críticas e opiniões tanto positivas quanto negativas de programadores sobre a linguagem {linguagem}',
            backstory=(
                "Você é um pesquisador experiente, com foco em entender como a referida linguagem de programação é percebida pela comunidade."
            ),
            verbose=True,
            memory=True,
            tools=[search_tool],
            allow_delegation=True
        )

        pesquisa_task = Task(
            description=(
                "Pesquise no Google por opiniões ou críticas tanto positivas quanto negativas feitas por programadores sobre a linguagem {linguagem}. "
                "Foque em fóruns, artigos de opinião e discussões técnicas com comentários reais de desenvolvedores."
            ),
            expected_output=(
                "Pelo menos 3 URLs que tem maior probabilidade de conter opiniões ou críticas tanto positivas quanto negativas de programadores sobre a linguagem {linguagem}."
            ),
            tools=[search_tool],
            agent=pesquisador
        )


        ### O EXTRATOR ###
        extrator = Agent(
            role='Extrator de conteúdo de URLs',
            goal='Extrair conteúdo de leitura de páginas da web',
            backstory=(
                "Você é especialista em extrair conteúdo limpo e legível de páginas web, removendo tudo que não é relevante para leitura."
            ),
            verbose=True,
            memory=True,
            tools=[scraper_tool],
            allow_delegation=False
        )

        extracao_task = Task(
            description=(
                "Acesse cada uma das URLs fornecidas pela tarefa anterior e extraia o conteúdo limpo e legível de cada URL. "
                "Remova qualquer conteúdo irrelevante como menus, rodapés ou anúncios."
            ),
            expected_output=(
                "Conteúdo limpo e legível de cada URL fornecida, pronto para ser trabalhado pelo redator."
            ),
            tools=[scraper_tool],
            agent=extrator
        )


        ### O COLETOR ###
        coletor = Agent(
            role='Coletor de opiniões ou críticas sobre a linguagem',
            goal='Encontrar as opiniões ou críticas tanto positivas como negativas sobre a linguagem {linguagem}.',
            backstory=(
                "Você é um coletor técnico com talento para compreender grandes volumes de informação, e encontrar o que é necessário para a futura redação."
            ),
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=False,
            llm=llm_4o_mini
        )

        coletagem_task = Task(
            description=(
                "Com base em todos os conteúdos extraídos das URLs, procure opiniões ou críticas positivas ou negativas sobre a linguagem."
                "Cada opinião ou crítica deve destacar os principais pontos mencionados pelos programadores, bem como qualquer percepção geral sobre a linguagem."
                "Não adicione comentários a parte,foque somente no conteúdo extraído."
            ),
            expected_output=(
                "Uma lista contendo 5 opiniões ou críticas sobre a linguagem, sendo 3 opiniões ou críticas positivas e 2 negativas."
                "Cada item deve deve ser citado também a fonte da informação, que pode ser o nome da empresa ou nome do site da onde se coletou a informação."
            ),
            tools=[],
            agent=coletor
        )


        ### O REDATOR ###
        redator = Agent(
            role='Redator Técnico',
            goal='Organizar as opiniões ou críticas tanto positivas como negativas sobre a linguagem {linguagem}',
            backstory=(
                "Você é um redator técnico com talento para organizar e resumir as informações coletadas, gerando assim uma boa redação final."
            ),
            verbose=True,
            memory=True,
            tools=[],
            allow_delegation=False,
            llm=llm_4o_mini
        )

        redacao_task = Task(
            description=(
                "Organize em forma de lista todas opiniões ou críticas positivas ou negativas coletadas sobre a linguagem."
                "Não adicione nenhum comentários a parte, fixe sua atenção somente em cima do conteúdo coletado."
            ),
            expected_output=(
                "Uma lista contendo 5 opiniões ou críticas sobre a linguagem no formato de bullet points, sendo 3 opiniões ou críticas positivas e 2 negativas, juntamente com a fonte da informação que pode ser o nome da empresa ou nome do site da onde se coletou a informação."
                "Cada item não deve ultrapassar 3 linhas, nem que para isso seja necessário aplicar um resumo sobre a informação."
                "Por fim relacionar também as URLs de onde foram extraídas as informações."
            ),
            tools=[],
            agent=redator
        )


        ### A EQUIPE ###
        crew = Crew(
            agents=[pesquisador, extrator, coletor, redator],
            tasks=[pesquisa_task, extracao_task, coletagem_task, redacao_task],
            output_log_file="crewlog.txt",
            process=Process.sequential
        )

        print("*** Execução da crew ***")
        # Execução da crew
        result = crew.kickoff(inputs={"linguagem": linguagem})
        print(result)