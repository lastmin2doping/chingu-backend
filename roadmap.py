import os
from google import genai
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("GENAI_API_KEY")
if not api_key:
    raise ValueError("API key not found. Please set GENAI_API_KEY in your .env file.")

def get_roadmap_for_aspiration(aspiration):
    prompt = f"""
    I want to achieve the following goal: "{aspiration}" 
    with a deadline of "{deadline}".

    Please create a **structured and logically ordered roadmap** that will allow me to complete this goal by the given deadline. 
    The roadmap should include:

    1. **High-level milestones**: Break down the goal into major phases or checkpoints.
    2. **Tasks/sub-tasks**: List actionable and practical steps for each milestone.
    3. **Time allocation**: Assign realistic time estimates to each task to fit within the deadline.
    4. **Skills required**: Specify skills that need to be learned or improved for each task.
    5. **Resources and references**: Recommend books, courses, websites, tools, or frameworks.
    6. **Tips and best practices**: Suggestions for staying productive, motivated, and avoiding common pitfalls.
    7. **Dependencies**: Indicate tasks that must be completed before others can start.
    8. **Progress tracking**: Suggest a way to measure completion and track progress.

    Please ensure the roadmap is **practically applicable, logically sequenced, and achievable within the deadline**.
    """


    try:
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    aspiration = input("Enter your goal/project: ")
    deadline = input("Enter your target completion date (YYYY-MM-DD): ")

    prompt = f"""
    I want to achieve the following goal: "{aspiration}" 
    with a deadline of "{deadline}".

    Please create a structured and logically ordered roadmap...
    (use the full template above)
    """

    roadmap = get_roadmap_for_aspiration(prompt)
    print(roadmap)

