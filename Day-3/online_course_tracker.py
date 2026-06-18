# Taking student details
name = input("Enter student name: ").strip()
course_name = input("Enter course name: ").strip()

# Course details stored in a tuple
course_info = (course_name, 12, "Prof. Sharma")

print("\nCourse Details")
print("Course     :", course_info[0])
print("Duration   :", course_info[1], "weeks")
print("Instructor :", course_info[2])

# Topics completed by the student
topics_input = input("\nEnter completed topics (comma separated): ")
completed_topics = [topic.strip() for topic in topics_input.split(",")]

all_topics = [
    "Python Basics",
    "Conditions",
    "Loops",
    "Data Structures",
    "Functions",
    "OOP",
    "File Handling",
    "Modules",
    "APIs",
    "Projects"
]

pending_topics = []

for topic in all_topics:
    if topic not in completed_topics:
        pending_topics.append(topic)

# Skills learned during the course
skills_input = input("\nEnter skills gained (comma separated): ")
skills_list = [skill.strip().lower() for skill in skills_input.split(",")]

unique_skills = set(skills_list)

course_skills = {"python", "programming", "problem solving"}
all_skills = unique_skills.union(course_skills)

scores = {}

print("\nEnter scores for completed topics")

for topic in completed_topics:
    score = int(input(f"Score for {topic}: "))
    scores[topic] = score

student_profile = {
    "name": name.title(),
    "course": course_info[0],
    "completed_topics": completed_topics,
    "pending_topics": pending_topics,
    "skills": all_skills,
    "scores": scores
}

if scores:
    average_score = sum(scores.values()) / len(scores)
    best_topic = max(scores, key=scores.get)
    weakest_topic = min(scores, key=scores.get)
else:
    average_score = 0
    best_topic = "N/A"
    weakest_topic = "N/A"

completion_percentage = (len(completed_topics) / len(all_topics)) * 100

print("\n" + "=" * 40)
print("STUDENT COURSE REPORT")
print("=" * 40)

print("Name       :", student_profile["name"])
print("Course     :", student_profile["course"])
print("Instructor :", course_info[2])

print("\nCompleted Topics:")
for topic in completed_topics:
    print("-", topic)

print("\nPending Topics:")
for topic in pending_topics:
    print("-", topic)

print(f"\nCourse Completion: {round(completion_percentage, 1)}%")

print("\nSkills:")
for skill in sorted(all_skills):
    print("-", skill)

print("\nScores:")
for topic, score in scores.items():
    print(f"{topic}: {score}/100")

print("\nAverage Score :", round(average_score, 2))
print("Best Topic    :", best_topic)
print("Weakest Topic :", weakest_topic)

choice = input("\nDo you want to add another completed topic? (yes/no): ").strip().lower()

if choice == "yes":
    new_topic = input("Enter topic name: ").strip()

    if new_topic in completed_topics:
        print("Topic already completed.")

    elif new_topic in all_topics:
        completed_topics.append(new_topic)
        pending_topics.remove(new_topic)

        student_profile["completed_topics"] = completed_topics
        student_profile["pending_topics"] = pending_topics

        print("Topic added successfully!")
        print("Updated pending topics:", pending_topics)

    else:
        completed_topics.append(new_topic)
        student_profile["completed_topics"] = completed_topics

        print("Topic added, but it is not part of the course syllabus.")

print("\nProgress saved.")
print("See you tomorrow!")