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

    if days <= 0:
        print("\n⚠️ Exam date should be in the future.")
        return

    total_chapters = sum(subjects.values())

    print("\n===================================")
    print(f"Hello {name}! 👋")
    print("Your AI Study Plan")
    print("===================================")

    print(f"Days available: {days}")
    print(f"Total chapters: {total_chapters}")
    print(f"Study hours/day: {hours:.1f}")

    chapters_per_day = max(1, round(total_chapters / days))

    print("\n📚 Recommended chapters per day:",
          chapters_per_day)

    print("\n-------- STUDY PLAN --------")

    chapter_count = 0

    for day in range(1, min(days, total_chapters) + 1):

        study_date = today + timedelta(days=day)

        for subject, chapter_total in subjects.items():

            if chapter_count >= total_chapters:
                break

            print(
                f"Day {day} | "
                f"{study_date.strftime('%d-%m-%Y')} | "
                f"{subject} | Chapter {(chapter_count % chapter_total) + 1}"
            )

            chapter_count += 1

    print("\n===================================")
    print("💡 AI Suggestions")
    print("===================================")

    if hours < 2:
        print("Try increasing your study time gradually.")

    elif hours >= 4:
        print("Great! Take short breaks between study sessions.")

    else:
        print("Your study time is good. Stay consistent.")

    print("\n✅ Follow the plan consistently!")
    print("===================================")


create_study_plan()