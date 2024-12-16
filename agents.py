import os
from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.7
)

# create a senior researcher agent with memory and verbose mode
news_researcher = Agent(
        role="Senior Researcher",
        goal="Uncover ground breaking technologies in {topic}",
        verbose=True,
        memory=True,
        backstory=( "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
        ),
        tools=[tool],
        llm=llm,
        allow_delegation=True
)

# creating a write agent with custom tools responsible in writing news blog
news_writer = Agent(
    role="Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=True,
    backstory=(
         "With a flair for simplifying complex topics, you craft"
         "engaging narratives that captivate and educate, bringing new"
         "discoveries to light in an accessible manner."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)