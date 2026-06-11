from model import llm
from prompt import prompt
from ml import results_text


chain = prompt | llm

response = chain.invoke({
    "results": results_text
    })

print(response.content)