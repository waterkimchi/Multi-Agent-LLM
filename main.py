from crewai import Crew, Process
from tasks import research_task, write_task
from agents import news_researcher, news_writer


def main():
    # forming the tech focused crew with some enhanced configuration
    crew = Crew(
        agents=[news_researcher, news_writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
    )

    result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
    print(result)

# starting the task execution process with enhanced feedback
if __name__ == "__main__":
    main()
