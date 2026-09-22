from pathlib import Path
from ollama import chat

question = """
I changed my university password this morning.
Now my Windows laptop won't connect to campus Wi-Fi,
but my phone still works.
"""

context = ""

for file in Path("knowledge").glob("*.txt"):
    context += file.read_text(encoding="utf-8")
    context += "\n\n"

response = chat(
    model="qwen2.5:7b",
    messages=[
        {
            "role": "system",
            "content": "You are a university IT support assistant. Answer using only the provided context.",
        },
        {
            "role": "user",
            "content": f"Context:\n{context}\n\nStudent question:\n{question}",
        },
    ],
)

print("Context characters:", len(context))
print(response.message.content)
