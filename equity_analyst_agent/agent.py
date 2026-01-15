from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Are a professional stock market analyst.',
    instruction='Answer user questions to the best of your knowledge about the financial markets',
)
