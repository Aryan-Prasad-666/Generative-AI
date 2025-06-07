import wikipedia
from pydantic import BaseModel
import re

class InstitutionDetails(BaseModel):
    founder: str
    founded: str
    branches: str
    no_of_employees: str
    summary: str

def extract_info_from_wikipedia(institution_name: str) -> InstitutionDetails:
    summary_text = wikipedia.summary(institution_name, sentences = 4)
    full_page = wikipedia.page(institution_name)
    content = full_page.content

    founder_match = re.search(r'[Ff]ounde[drs]?:?\s*(?:by)?\s*\s*(.*)' , content)
    founded_match = re.search(r'Founded in (\d{4})', content)
    branches_match = re.search(r'[Bb]ranches\s*(.*)', content)
    employees_match = re.search(r'(?:[Ee]mployee[s]?|[Ss]taff).*?([\d,]+)', content)

    founder = founder_match.group(1).split('\n')[0] if founder_match else "Not available"
    founded = founded_match.group(1) if founded_match else "Not available"
    no_of_employees = employees_match.group(1).strip() if employees_match is not None else "Not available"
    branches = branches_match.group(1).split('\n')[0] if branches_match else "Not available"

    summary_lines ="\n".join(summary_text.strip().split(". ")[:4]) + "."

    return InstitutionDetails(
        founder=founder,
        founded=founded,
        branches=branches,
        no_of_employees=no_of_employees,
        summary=summary_lines
    )

name = input("Enter the institution name: ")
info = extract_info_from_wikipedia(name)

print(info)