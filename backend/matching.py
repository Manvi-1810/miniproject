# Import the skill extraction function.
from resume_parser import extract_skills


def match_resume_to_job(resume_text, required_skills):
    """
    Compare resume skills with job requirements.
    Returns a score and an explanation of the results.
    """

    # Extract skills mentioned in the resume.
    resume_skills = extract_skills(resume_text)

    # Normalize skills to avoid case-sensitive comparisons.
    resume_set = {skill.lower() for skill in resume_skills}
    required_set = {skill.lower() for skill in required_skills}

    # Find skills that match the job requirements.
    matched = [
        skill for skill in required_skills
        if skill.lower() in resume_set
    ]

    # Find required skills not identified in the resume.
    missing = [
        skill for skill in required_skills
        if skill.lower() not in resume_set
    ]

    # Calculate the percentage of required skills matched.
    score = round((len(matched) / len(required_skills)) * 100) if required_skills else 0

    # Return the score and transparent explanation.
    return {
        "match_score": score,
        "resume_skills": resume_skills,
        "matched_skills": matched,
        "skills_not_identified": missing
    }