name = 'Blue agent'
challenge = 'Deploy a new blue agent. The agent should successfully beacon back to this server instance.'
extra_info = """Most Endpoint Detection and Response products use agents that are installed on the endpoints that need
to be protected. Sandcat can function as Caldera's Blue agent too."""


async def verify(services):
    agents = await services.get('data_svc').locate('agents')
    return True if any(agent.group == 'blue' for agent in agents) else False