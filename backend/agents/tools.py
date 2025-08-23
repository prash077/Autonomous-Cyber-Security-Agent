import subprocess
from crewai_tools import BaseTool

class TerminalTool(BaseTool):
    name: str = "Terminal Tool"
    description: str = "Executes a terminal command and returns its output."
    
    def _run(self, command: str) -> str:
        try:
            result = subprocess.run(
                command.split(),
                check=True,
                capture_output=True,
                text=True
            )
            return f"Command executed successfully. Output:\n{result.stdout}"
        except subprocess.CalledProcessError as e:
            return f"Command failed with exit code {e.returncode}. Stderr:\n{e.stderr}"
        except FileNotFoundError:
            return f"Command not found: {command}"