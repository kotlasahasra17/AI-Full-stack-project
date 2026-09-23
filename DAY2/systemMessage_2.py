import ollama
response= ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"system",
            "content":" You are teacging a 5 year old child. Give the answers in 2-3 lines only"
        },
        {
            "role":"user",
            "content":"Explain ml"
        }
    ]
)
print(response["message"]["content"])