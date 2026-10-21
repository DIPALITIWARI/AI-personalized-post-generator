
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm
import json


def extract_metadata(text):
    prompt_template = '''
    You are given a LinkedIn post. Extract the following metadata:

1. line_count: Number of lines in the post.
2. language: Return "en" for English, "hinglish" for Hindi + English.
   For any other language, return "en".
3. tags: Extract exactly two relevant tags.

IMPORTANT:
- Return ONLY a valid JSON object.
- Do not use Markdown formatting or code fences.
- Do not add any explanation.
- Use double quotes for all JSON keys and string values.

Required format:
{{
    "line_count": 1,
    "language": "en",
    "tags": ["MachineLearning", "AI"]
}}

LinkedIn Post: {text}
''' 

    pt = PromptTemplate.from_template(template=prompt_template)
    chain = pt | llm

    response = chain.invoke({"text": text})

    json_parser = JsonOutputParser()

    try:
        metadata = json_parser.parse(response.content)
        return metadata

    except OutputParserException as e:
        print(f"Output parsing error: {e}")
        return {
            "line_count": len(text.splitlines()),
            "language": "en",
            "tags": []
        }


def process(raw_file, output_file):
    enriched_post = []

    with open(raw_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

        for item in data:
            post = {
                'text': item['text'],
                'engagement': item['engagement']
            }

            metadata = extract_metadata(item['text'])

            post_with_metadata = post | metadata
            enriched_post.append(post_with_metadata)

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(enriched_post, f, indent=4, ensure_ascii=False)

    for epost in enriched_post:
        print(epost)


if __name__ == "__main__":
    raw_file = "data/raw_data.json"
    output_file = "processed_data.json"

    process(raw_file, output_file)
