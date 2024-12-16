from dotenv import load_dotenv

import google.generativeai as gemini
import asyncio as asyn
import os


# load the environment variables
load_dotenv()

# api key from .env
AI_KEY = os.getenv("GEMINI_API_KEY")

# gemini configuration
gemini.configure(api_key=AI_KEY)

class Agent:

    # init
    def __init__(self, agent_id, model_name="gemini-1.5-flash"):
        self.agent_id = agent_id
        self.model = gemini.GenerativeModel(model_name)
        self.memory = []  # Store the agent's previous interactions or knowledge
    
    # generate an action from a given prompt
    async def generate(self, prompt):
        try:
            return self.model.generate_content(prompt).text
        except Exception as e:
            return e
        
    # interact with another agent by exchanging prompts
    async def interact(self, other_agent):
        prompt = f"Agent {self.agent_id} wants to collaborate with you on writing a codebase to test multi-agent LLM simulation, Agent {other_agent.agent_id}. Respond with an idea."

        # TODO: create a action prompt to interact with the other agent

        response = await other_agent.generate(prompt)

        # append memory as a prompt
        # TODO: edit the memory format
        self.memory.append(f"Interaction with Agent {other_agent.agent_id}: {response}")
        return response