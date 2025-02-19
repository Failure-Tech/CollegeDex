# # import openai

# # # Replace with your own OpenAI API key
# # openai.api_key = "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"

# # # Define the prompt
# # prompt = "Roast the absolute shit out of these college activities/statistics that will be given as prompts"

# # # Interact with OpenAI's API
# # response = openai.Completion.create(
# #     engine="text-davinci-003",  # Ensure you're using a compatible engine
# #     prompt=prompt,
# #     max_tokens=100,  # You can adjust this parameter
# #     temperature=0.7  # Controls randomness, adjust between 0 to 1
# # )

# # # Extract the response text
# # output_text = response['choices'][0]['text'].strip()
# # print(output_text)

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

# print(completion.choices[0].message.content)

import openai

# Define your OpenAI API key
openai.api_key = "your-openai-api-key"

def get_chanceme_response(user_input: str) -> str:
    """Uses OpenAI to generate a response to the user input."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a bot that roasts college activities/statistics."
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        max_tokens=100,
        temperature=0.7
    )
    return response['choices'][0]['message']['content'].strip()

print(openai.__version__)