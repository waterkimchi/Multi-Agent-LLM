import environment as env_obj
import agent as agent_obj
import asyncio

async def main():
    env = env_obj.Environment()

    for i in range(3):
        agent = agent_obj.Agent(agent_id=i)
        env.add_agent(agent)

    await env.simulate(num_interactions=4)

if __name__ == "__main__":
    asyncio.run(main())
