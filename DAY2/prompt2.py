import ollama
response= ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"Define AI in 2 lines and 3 main types of AI in bullet points "
        }
    ]
)
print(response["message"]["content"])