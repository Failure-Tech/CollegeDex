# import openai

# # optional; defaults to `os.environ['OPENAI_API_KEY']`
# openai.api_key = "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"

# # all client options can be configured just like the `OpenAI` instantiation counterpart
# # openai.base_url = "https://..."
# openai.default_headers = {"x-foo": "true"}

# content = ""

# completion = openai.chat.completions.create(
#     model="gpt-4",
#     messages=[
#         {
#             "role": "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",
#             "content": "Roast the absolute shit out of these college activities/statistics that will be given as prompts"
#         },
#         {
#             "role": "user",
#             "content": content,
#         },
#     ],
# )

# print(completion.choices[0].message.content

# import os
# import json
from groq import Groq
from typing import Dict, Any

def create_groq_client() -> Groq:
    """Create and validate the Groq client."""
    api_key = "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"
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable not set")
    return Groq(api_key=api_key)

def get_chanceme_response(client: Groq, user_prompt: str) -> str:
    """Generate a response from the Groq API."""
    try:
        messages = [
            {
                "role": "system",
                # "content": "Roast the absolute shit out of these college activities/statistics that will be given as prompts, please curse (fuck, shit, etc.) as much as possible and be as mean as possible."
                "content": "Roast the absolute shit out of these college activities/statistics that will be given as prompts"
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ]
        response = client.chat.completions.create(
            messages=messages,
            model="gemma2-9b-it",  # Example model
            # model="llama-3.1-8b-instant",
            temperature=0.7,
            
        )
        content = response.choices[0].message.content
        if not content:
            raise ValueError("Reduce size of chanceme")

        return content
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")

# def main():
#     try:
#         # Initialize Groq client
#         print("Initializing Groq client...")
#         client = create_groq_client()
#         print("Groq client initialized")

#         # Example user input
#         user_input = "Discuss the effectiveness of college sports programs."
        
#         # Generate response
#         print("Generating response...")
#         response = generate_response(client, user_input)
#         print("Response received:")
#         print(response)

#     except Exception as e:
#         print(f"\nError: {str(e)}")

# if __name__ == "__main__":
#     main()