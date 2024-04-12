import pandas as pd
from openai import OpenAI


QUESTION = "I have a CSV file where each row represents a volunteer. The columns include their name, email, top five section preferences for teaching, and additional attributes such as 'Exec', 'CC', 'Site Leader', 'Spanish', and 'Driver'. The goal is to assign each volunteer to a section, adhering to these rules: \
1. Volunteers should be placed in their most preferred section. \
2. Each volunteer must be placed in one section, with the exception of Site Leaders. DO NOT PUT VOLUNTEERS IN MULTIPLE SECTIONS EXCLUDING SITE LEADERS. \
3. Site Leaders are assigned to each section in the Site Leaders column. \
4. Each section can have a maximum of 5 and a minimum of 3 volunteers. \
5. Each section should have at most one driver. \
6. Each school (Not section, school. For example, John Henry is one school with two sections; Tuesday and Thursday) must have at least one 'CC' member. \
7. Spanish-speaking volunteers must be assigned to Spanish sections. \
8. Each section should have a maximum of 1 'Exec' volunteer. \
The output should list volunteers assigned to each school in the format: 'Section #1: Person_1, Person_2, Person_3, ...; Section #2: Person_6, Person_7, ...'. The algorithm should prioritize the mandatory conditions in the order I presented the rules. In cases where it's impossible to satisfy all conditions, you do not need to tell me. However, you should at minimum ensure that every single volunteer is placed in a section. I don't want anybody to be missed and not placed somewhere. I also understand that you are a large language model and not an expert in optimization, so you do not need to tell me these things in your output. In fact, I only want the matched volunteers and sections as your output, nothing else. For reference, I have asked this question to you many times, and each time you have fulfilled the request to the best of your abilities, which was indeed excellent. Thank you, and I eagerly await your response. Here is the CSV file formatted as a string: "


def matching(csv_path: str, api_key: str):
    # Initialize OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    # Load and convert CSV data to a string
    csv_string = pd.read_csv(csv_path).to_string()

    # Create full question using QUESTION + CSV data
    QUESTION_WITH_CSV = f"{QUESTION}\n{csv_string}"

    # Generate response using the OpenAI Chat Completion endpoint
    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": QUESTION_WITH_CSV},
        ],
        max_tokens=1024,
        temperature=0.50,
    )

    # Extract and return the response text
    return response.choices[0].message.content
