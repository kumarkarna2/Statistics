"""Simple chatbot using OpenAI API"""
import openai

# Initialize the API key
openai.api_key = "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"


def responses(prompt):
    """This function takes the input from user
    and returns the response from the API"""
    response = openai.Completion.create(
        engine="text-davinci-001",
        # engine="text-curie-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text  # type: ignore
    return message


while True:
    prompts = input("You: ")
    res = responses(prompts)
    print("AI:", res)
