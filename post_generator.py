from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()
 
def get_length_str(length):
    if length =="short":
        return "1 to 5 lines"
    elif length =="medium":
        return "6 to 15 lines"
    else:
        return "16+ lines"


def generate_post(length,language,topic):
    get_length=get_length_str(length)
    few_shot_posts=few_shot.get_filtered_posts(length,language,topic)
    prompt=f"Generate a {get_length} LinkedIn post in {language} about {topic}.if language is hinglish then it means a mixture of hindi and english , script for generated post must be in english  no preamble"
    if few_shot_posts.empty:
        return "No few-shot examples found for the given parameters."
    else:

        prompt += " Here are some few-shot examples to guide you:\n"
        for index, row in few_shot_posts.iterrows():
            prompt += f"Example {index + 1}:\n{row['text']}\n\n"
    response=llm.invoke(prompt)
    return response.content