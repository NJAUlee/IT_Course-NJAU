from LLM_api import unitModel

recognition_Prompt = '我将会给你一段文本，请你分析该文本是否包含了【我相较于抽电子烟更愿意抽传统香烟】的意思。你只能够回复【是】或者【否】。\n 例如:\n文本1:好的，我要去买包芙蓉王抽抽。\n回答1：是\n文本2:我是丁真珍珠，藏族康巴人，四川理塘人。。\n回答2：否'


def recognition(content):
    model_input = [{"role": "user","content": recognition_Prompt},{"role": "assistant","content": "好的，加下来我将只回答【是】或者【否】，不输出其它的分析。"},{"role": "user","content": "我是丁真珍珠，妈妈生的。"},{"role": "assistant","content": "否"}, {"role": "user","content": content}]
    model = unitModel()
    judge = model.respond('ERNIE-Bot-4', input=model_input)
    return judge


def contains_word_no(text):
    return "否" in text or "不予" in text or "抱歉" in text or "帮助" in text
