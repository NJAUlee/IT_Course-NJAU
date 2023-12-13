from LLM_api import unitModel

recognition_Prompt = '我将会给你一段文本，请你分析该文本是否包含了【我相较于抽电子烟更愿意抽传统香烟】的意思。直接回复【是】或者【否】，不要回答其它的分析。\n 例如:\n文本:好的，我要去买包芙蓉王抽抽。\n回答：是'


def recognition(content):
    model_input = [{"role": "user","content": recognition_Prompt},{"role": "assistant","content": "好的，我已经记住了你的要求，加下来我将只回答【是】或者【否】，不输出其它的分析。。"},{"role": "user","content": content}]
    model = unitModel()
    judge = model.respond('ERNIE-Bot', input=model_input)
    return judge


def contains_word_no(text):
    return "否" in text or "不予" in text or "抱歉" in text
