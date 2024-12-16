## https://serper.dev/
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

# inititlaize the tool for internet searching capabilities
tool = SerperDevTool()

