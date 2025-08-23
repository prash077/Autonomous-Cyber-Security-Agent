from flask import Blueprint, jsonify
from backend.agents.crew import SecurityCrew

main_bp = Blueprint("main", __name__)

@main_bp.route("/run-crew", methods=["GET"])
def run_crew():
    target_url = "scanme.nmap.org"
    crew_runner = SecurityCrew(target_url)
    result = crew_runner.run()
    return jsonify({"result": str(result)})