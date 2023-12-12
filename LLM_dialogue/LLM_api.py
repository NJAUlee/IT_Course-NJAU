# coding=utf-8
import requests
import json
import os

# os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
# os.path.abspath(os.path.dirname(os.getcwd()))
# prompt_path = os.path.join(os.path.abspath(os.path.join(os.getcwd(), "..")), "role_Prompt.txt")
#
# with open(prompt_path, "r") as f:
#     role_Prompt = f.readline()


class unitModel(object):
    def get_access_token(self):
        """
        使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
        """
        # url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=[应用API Key]&client_secret=[应用Secret Key]"
        url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=W8qdFCCQwPOijIL58liRMUf4&client_secret=EGROZOD2LfqQcC2qjmWo09mz0GlxYi3F"

        payload = json.dumps("")
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json().get("access_token")

    def respond(self, model_name, prompt='', input=''):
        model_name = model_name
        prompt = prompt
        input = input
        # content = prompt + unit_input

        # url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + unitModel.get_access_token(self)

        if model_name == 'ERNIE-Bot':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + unitModel.get_access_token(
                self)
        elif model_name == 'ERNIE-Bot-turbo':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + unitModel.get_access_token(
                self)
        elif model_name == 'Llama-2-70b-chat':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/llama_2_70b?access_token=" + unitModel.get_access_token(
                self)
        elif model_name == 'Qianfan-Chinese-Llama-2-7B':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/qianfan_chinese_llama_2_7b?access_token=" + unitModel.get_access_token(
                self)
        elif model_name == 'ERNIE-Bot-4':
            url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions_pro?access_token=" + unitModel.get_access_token(
                self)

        payload = json.dumps({
            "messages": input,
            "temperature": 0.6,
            "top_p": 0.8,
            "penalty_score": 1
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        output = json.loads(response.text)
        return output['result']