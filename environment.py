import random
import asyncio

class Environment:

    def __init__(self):
        self.agents = []
    
    def add_agent(self, agent):
        self.agents.append(agent)
    
    async def simulate(self, num_interactions):
        tasks = []
        for _ in range(num_interactions):
            agent1, agent2 = random.sample(self.agents, 2)  # Pick two random agents
            print(f"Agent {agent1.agent_id} interacting with Agent {agent2.agent_id}")
            tasks.append(self.run_interaction(agent1, agent2))
        await asyncio.gather(*tasks)
    
    async def run_interaction(self, agent1, agent2):
        response = await agent1.interact(agent2)
        print(f"Agent {agent1.agent_id} received: {response}")
    
