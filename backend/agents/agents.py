# from crewai import Agent
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()


# class SecurityAgents:
#     def __init__(self):
#         self.llm = "gemini/gemini-1.5-pro"

#     def planner_agent(self):
#         return Agent(
#             role="Cyber-Security Planner",
#             goal="Analyze the user's request and create a detailed, prioritized plan for a simulated penetration test.",
#             backstory=(
#                 "You are a seasoned cybersecurity strategist. Your expertise lies in breaking down complex security assessments "
#                 "into logical, actionable steps. You specialize in creating comprehensive plans for your team."
#             ),
#             verbose=True,
#             allow_delegation=True,
#             llm=self.llm
#         )

#     def recon_agent(self):
#         return Agent(
#             role="Reconnaissance Specialist",
#             goal="Gather as much public information as possible about the target, including open ports and services.",
#             backstory=(
#                 "You are a master of open-source intelligence (OSINT). You meticulously scan and gather data "
#                 "to create a detailed map of the target's attack surface. Your work is the foundation for all subsequent actions."
#             ),
#             verbose=True,
#             allow_delegation=False,
#             llm=self.llm
#         )


from crewai import Agent
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class SecurityAgents:
    def __init__(self):
        self.llm = "gemini/gemini-1.5-flash"

    def planner_agent(self):
        return Agent(
            role="Cyber-Security Planner",
            goal="Analyze the user's request and create a detailed, prioritized plan for a simulated penetration test.",
            backstory=(
                "You are a seasoned cybersecurity strategist. Your expertise lies in breaking down complex security "
                "assessments into logical, actionable steps."
            ),
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )

    def recon_agent(self):
        return Agent(
            role="Reconnaissance Specialist",
            goal="Gather as much public information as possible about the target, including open ports and services.",
            backstory=(
                "You are a master of open-source intelligence (OSINT). You meticulously scan and gather data "
                "to create a detailed map of the target's attack surface."
            ),
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
