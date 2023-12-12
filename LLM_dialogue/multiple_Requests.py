# coding=utf-8
import os


def init_memory():
    os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    os.path.abspath(os.path.dirname(os.getcwd()))
    memory_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), "memory.txt")
    prompt_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), "role_Prompt.txt")

    with open(prompt_path, "r") as f:
        role_Prompt = f.readline()

    with open(memory_path, "r") as f:
        memory = eval(f.read())

    return memory


def question(quest='', memory=[]):
    the_question = {"role": "user", "content": quest}
    memory = memory.append(the_question)
    return memory


def answer(ans='', memory=[]):
    the_answer = {"role": "assistant", "content": ans}
    memory = memory.append(the_answer)
    print(ans)
    return memory
