import sys

sys.path.append('.')

from core.vector_store import model
from crewai import Agent, Task, Crew, Process
from crewai_tools import CodeDocsSearchTool
from core.vector_store import agent_executor

def main():
    # Initialize the tool
    # tool = CodeDocsSearchTool(
    #     docs_url='https://docs.conductor-oss.org/devguide/concepts/',
    #     config=dict(
    #         llm=dict(
    #             provider="ollama",
    #             config=dict(
    #                 model="llama3.1",
    #                 temperature=0.5,
    #                 top_p=1,
    #                 # stream=true,
    #             ),
    #         ),
    #         embedder=dict(
    #             provider="ollama",
    #             config=dict(
    #                 model="nomic-embed-text"
    #             ),
    #         ),
    #     )
    # )
    #
    # # Create the agent
    # technical_assistant = Agent(
    #     role='Technical Assistant',
    #     goal='Assist with general question and answers on the netflix conductor using documentation.',
    #     verbose=True,
    #     backstory='You are an expert of the netflix conductor.',
    #     tools=[tool],
    #     llm=model
    # )
    #
    # # Define the task
    # tech_help_task = Task(
    #     description="Provide detail answers based on the documentation.",
    #     expected_output="A detailed answer to the query.",
    #     tools=[tool],
    #     agent=technical_assistant,
    # )
    #
    # # Form the crew and execute
    # crew = Crew(
    #     agents=[technical_assistant],
    #     tasks=[tech_help_task],
    #     process=Process.sequential
    # )
    #
    # # Example query
    # result = crew.kickoff(inputs={'question': 'What are different type of tasks in Conductor?'})
    result = agent_executor.invoke({"input": "hi!", "context": "soemthing"})
    print(result)


if __name__ == "__main__":
    main()
