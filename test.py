import os
from openai import OpenAI
import dotenv

# 1. Install the OpenAI Python library if you haven't already:
#    pip install --upgrade openai

# 2. Set your API key (you can also set OPENAI_API_KEY as an env var)
dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# 3. Retrieve the list of available models
response = openai.Model.list()

# 4. Print each model’s ID
for model in response["data"]:
    print(model["id"])
