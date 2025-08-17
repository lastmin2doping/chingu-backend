import requests
from google import genai

def get_roadmap_for_aspiration(aspiration):
    """
    Use Gemini API to generate a detailed roadmap for the user's entered aspiration.
    The roadmap should include key steps, recommended resources, skills to learn, and a timeline.
    """
    prompt = f"""
    I want to achieve the following aspiration: "{aspiration}"

    Please provide a detailed roadmap to achieve this goal. 
    Include:
    - Key steps and milestones
    - Recommended resources (books, websites, courses)
    - Important skills to learn
    - Suggested timeline for each step
    - Tips for staying motivated and overcoming common challenges

    Format the response in a clear, structured way.
    """

    try:
        # Initialize the GenAI client
        client = genai.Client(api_key="AIzaSyDIefdOVwNJMtitlEfwOeJQwLqZzhUubGQ")  # Replace with your actual API key

        # Generate content using the Gemini model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return None