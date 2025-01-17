from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.1")

response  = model.invoke(input='хто ти?')
print(response)