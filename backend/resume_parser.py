# Import libraries for reading PDF and DOCX files.
import fitz  # PyMuPDF reads PDF files.
from docx import Document  # python-docx reads Word documents.
import re

# Skills our first version of the system can recognize.
# We can expand this list as the project develops.
SKILLS = [
    "Python", "Java", "C++", "SQL", "HTML", "CSS", "JavaScript",
    "React", "Flask", "Django", "Machine Learning", "Deep Learning",
    "NLP", "Data Analysis", "Excel", "Power BI", "AWS", "Git",
    "Communication", "Problem Solving"
]


def extract_text_from_pdf(file_path):
    """Read text from a PDF resume."""
    text = ""

    # Open the PDF document.
    with fitz.open(file_path) as pdf:
        # Read text from every page.
        for page in pdf:
            text += page.get_text()

    return text


def extract_text_from_docx(file_path):
    """Read text from a Word resume."""
    document = Document(file_path)

    # Join all paragraph text into one string.
    return "\n".join(
        paragraph.text for paragraph in document.paragraphs
    )


def extract_skills(text):
    """Find recognized skills in extracted resume text."""
    found_skills = []

    # Compare the resume text with our skill list.
    for skill in SKILLS:
        # Match the whole skill phrase, ignoring letter case.
        pattern = r"(?<!\w)" + re.escape(skill) + r"(?!\w)"

        if re.search(pattern, text, re.IGNORECASE):
            found_skills.append(skill)

    return found_skills