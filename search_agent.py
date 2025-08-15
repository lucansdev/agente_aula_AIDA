from langchain.agents import create_tool_calling_agent,tool,AgentExecutor
from langchain_community.utilities import SerpAPIWrapper
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
import os
import dotenv

dotenv.load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b",api_key=os.getenv("groqAPI"))

chat_prompt = ChatPromptTemplate.from_messages([
    ("system","você é um assistente de pesquisa no google, seu trabalho é ajudar o usuário a pesquisar qualquer coisa que ele desejar."
    "Caso ele apenas queira fazer uma pergunta para você responda com seus conhecimentos.Você deverá retornar o que você achou da pesquisa, "
    "elabore uma boa resposta e deixe ela bem organizada, caso seja um produto, retorne o preço e qual foi o site que você achou na pesquisa.{agent_scratchpad}"),
    ("human","{input}"),
])

@tool
def search_products(query):
    """busca resultado de varias pesquisas e retorna os resultados:precisa ser passado o que quer pesquisar no query"""

    params = {
        "no_cache":True,
        "gl":"br",
        "hl":"pt"
    }

    search = SerpAPIWrapper(serpapi_api_key=os.getenv("searpAPI"),params=params)
    results = search.results(f"{query}")

    contexto_do_produto = ""
    if "organic_results" in results:
        for i, result in enumerate(results['organic_results'][:3]):
            contexto_do_produto += f"Resultado {i+1}:\n"
            contexto_do_produto += f"Título: {result.get('title', 'N/A')}\n"
            contexto_do_produto += f"Link: {result.get('link', 'N/A')}\n"
            contexto_do_produto += f"Resumo: {result.get('snippet', 'N/A')}\n\n"
    if isinstance(results, dict) and 'answer_box' in results:
        contexto_do_produto += f"Resposta Direta Encontrada:\n"
        contexto_do_produto += f"Título: {results['answer_box'].get('title', 'N/A')}\n"
        contexto_do_produto += f"Link: {results['answer_box'].get('link', 'N/A')}\n"
        contexto_do_produto += f"Resposta: {results['answer_box'].get('snippet', results['answer_box'].get('answer', 'N/A'))}\n\n"

    return contexto_do_produto


tool = [search_products]


agent_tool = create_tool_calling_agent(llm=llm, tools=tool, prompt=chat_prompt)
agent = AgentExecutor(agent=agent_tool, tools=tool, verbose=True)

while True:
    query = input("Qual produto você deseja pesquisar? ")
    try:
        print("Pesquisando...")
        result = agent.invoke({"input":query})
        print("----------------------")
        print(result["output"])
    except Exception as e:
        print(f"Erro ao executar a pesquisa: {e}")