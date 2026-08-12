AI Contribution Log
Contribution ID: 001

Date: 12 August 2026
File: study_planner.py
AI Tool: GitHub Copilot

Prompt/Comment:
Create a simple AI study planner in Python.

AI Suggestion:
Generated the create_study_plan() function with user input, subject details, chapters, study hours, and exam date.

Accepted: Yes
Modified: Yes

Modification:
Reviewed and organized the generated input section.

Reason:
To collect all information required to create a personalized study plan.

Contribution ID: 002

Date: 12 August 2026
File: study_planner.py
AI Tool: GitHub Copilot

Prompt/Comment:
Calculate the number of days available before the exam.

AI Suggestion:
Used datetime and timedelta to calculate the remaining study days.

Accepted: Yes
Modified: Yes

Modification:
Added validation to check whether the exam date is in the future.

Reason:
To prevent invalid exam dates and calculate the available preparation time correctly.

Contribution ID: 003

Date: 12 August 2026
File: study_planner.py
AI Tool: GitHub Copilot

Prompt/Comment:
Generate a study plan based on subjects, chapters, and available days.

AI Suggestion:
Generated logic to calculate total chapters, chapters per day, and create a daily schedule.

Accepted: Yes
Modified: Yes

Modification:
Reviewed the loop and adjusted the study-plan output.

Reason:
To automatically distribute chapters across the available study days.

Contribution ID: 004

Date: 12 August 2026
File: study_planner.py
AI Tool: GitHub Copilot

Prompt/Comment:
Add study suggestions according to daily study hours.

AI Suggestion:
Added conditions for less than 2 hours, 2–4 hours, and 4 or more hours of study.

Accepted: Yes
Modified: Yes

Modification:
Reviewed and accepted the suggested messages.

Reason:
To provide simple personalized advice to the student.

Contribution ID: 005

Date: 12 August 2026
File: study_planner.py
AI Tool: GitHub Copilot

Prompt/Comment:
Improve the presentation of the study planner output.

AI Suggestion:
Added headings, formatted dates, emojis, and clear study-plan sections.

Accepted: Yes
Modified: Yes

Modification:
Reviewed the final output format and tested the program with sample inputs.

Reason:
To make the study plan clear, readable, and user-friendly. 
Code Given by AI
from datetime import datetime, timedelta

def create_study_plan():
    print("===================================")
    print("       🤖 AI STUDY PLANNER")
    print("===================================")

    name = input("Enter your name: ")
    subjects = {}

    n = int(input("\nEnter number of subjects: "))

    for i in range(n):
        subject = input(f"\nEnter subject {i + 1}: ")
        chapters = int(input(f"Enter number of chapters in {subject}: "))
        subjects[subject] = chapters

    hours = float(input("\nHow many hours can you study per day? "))
    exam_date = input("Enter exam date (DD-MM-YYYY): ")

    exam = datetime.strptime(exam_date, "%d-%m-%Y")
    today = datetime.now()
    days = (exam - today).days
    Code Modified by Me
    if days <= 0:
    print("\n⚠️ Exam date should be in the future.")
    return

total_chapters = sum(subjects.values())
chapters_per_day = max(1, round(total_chapters / days))
Reason for Modification:
Added validation and improved the study-plan calculation to make the program more reliable.

Overall Contribution

AI was used to generate the initial code and logic. I reviewed, understood, tested, and modified the generated code to meet the requirements of my AI Study Planner project.
