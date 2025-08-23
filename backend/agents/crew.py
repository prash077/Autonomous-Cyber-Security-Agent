from crewai import Crew, Process
from .agents import SecurityAgents
from .tasks import SecurityTasks

class SecurityCrew:
    def __init__(self, target_url):
        self.target_url = target_url

    def run(self):
        agents = SecurityAgents()
        tasks = SecurityTasks(self.target_url)

        crew = Crew(
            agents=[
                agents.planner_agent(),
                agents.recon_agent(),
            ],
            tasks=[
                tasks.recon_task(agents.recon_agent()),
            ],
            process=Process.sequential,
            verbose=2,
            full_output=True,
        )

        result = crew.kickoff()
        return result