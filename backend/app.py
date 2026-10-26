# Import Flask tools.
from flask import Flask, jsonify, request

# Import our resume matching function.
from matching import match_resume_to_job

# Create the Flask application BEFORE using @app.route.
app = Flask(__name__)


# Test whether the backend is running.
@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "success",
        "message": "AI Recruitment Backend is running!"
    })


# Match resume text against job requirements.
@app.route("/api/match", methods=["POST"])
def match_resume():
    # Read the JSON data sent by the frontend or test request.
    data = request.get_json(silent=True) or {}

    resume_text = data.get("resume_text", "")
    required_skills = data.get("required_skills", [])

    # Check that the received data has the correct types.
    if not isinstance(resume_text, str) or not isinstance(required_skills, list):
        return jsonify({"error": "Invalid input format"}), 400

    # Calculate the matching score and explanations.
    result = match_resume_to_job(resume_text, required_skills)

    return jsonify(result)


# Start the development server when this file is run directly.
if __name__ == "__main__":
    app.run(debug=True, port=5000)