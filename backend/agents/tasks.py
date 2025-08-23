from crewai import Task
from .tools import TerminalTool

class SecurityTasks:
    def __init__(self, target_url):
        self.target_url = target_url
        self.terminal_tool = TerminalTool()

    def recon_task(self, agent):
        return Task(
            description=(
                f"Identify open ports and running services on the target: {self.target_url}. "
                "Use the Terminal Tool to run an nmap scan. "
                "Output the results of the scan in a clear, formatted summary."
            ),
            expected_output=(
                "A detailed summary of open ports, services, and versions found on the target URL. "
                "Example: 'Port 80 (HTTP) - Nginx 1.25.3, Port 443 (HTTPS) - Apache 2.4.38...'"
            ),
            agent=agent,
            tools=[self.terminal_tool]
        )