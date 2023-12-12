from LLM_api import unitModel
from multiple_Requests import init_memory,question,answer

memory = init_memory()
my_model = unitModel()

while True:
    user_Question = input("你想说点什么(输入'退出'，即可关闭对话)：")
    question(memory=memory, quest=user_Question)
    if user_Question == '退出':
        print("对话已关闭！")
        break
    else:
        llm_Answer = my_model.respond('ERNIE-Bot', input=memory)
        answer(memory=memory, ans=llm_Answer)
        print(llm_Answer)