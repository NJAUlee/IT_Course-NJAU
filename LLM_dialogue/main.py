from LLM_api import unitModel

my_model = unitModel()

question = input("你想说点什么：")
answer = my_model.respond('ERNIE-Bot', unit_input=question)

print(answer)