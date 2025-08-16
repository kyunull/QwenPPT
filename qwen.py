import requests
import json
import os
from config import Config

# def get_access_token():
#     """
#     使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
#     """
#     API_Key = Config.API_Key
#     Secret_Key = Config.Secret_Key
#     url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={API_Key}&client_secret={Secret_Key}".format(API_Key=API_Key,Secret_Key=Secret_Key)
#
#     payload = json.dumps("")
#     headers = {
#         'Content-Type': 'application/json',
#         'Accept': 'application/json'
#     }
#
#     response = requests.request("POST", url, headers=headers, data=payload)
#     return response.json().get("access_token")

def qwen_api(message,use4=False):
    API_Key = Config.API_Key
    if use4:
        url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
    else:

        url = "https://dashscope.aliyuncs.com/api/v1/services/aigc/multimodal-generation/generation"
    payload = json.dumps({
        "model": "qwen-vl-max",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [{"text":message}]
                }
            ]
        } ,
        "parameters": {
            "use_raw_prompt": True
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_Key,
        "X-DashScope-Api-Key": API_Key
    }
    # try:
    #     response = requests.request("POST", url, headers=headers, data=payload)
    #     result = response.json().output.choices[0].message.content[0].text
    #     print("完整响应：", result)
    # except Exception as e:
    #     print("异常响应：",response.text)
    # #     print("API请求异常：", e)
    #     result = "error"
    # # print(result)

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        result = response.json()["output"]["choices"][0]["message"]["content"][0]["text"]
        print("完整响应：", result)
    else:
        print("异常响应：",response.text)
    return result

def yiyan_embedding(input_text):
    if input_text=="":
        input_text="  "
    url = "https://qianfan.baidubce.com/v2/chat/completions"

    payload = json.dumps({
        "input": [input_text]
    })
    headers = {
        'Content-Type': 'application/json',
         'Authorization': 'Bearer ' + Config.API_Key
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    result = response.json()["output"]["choices"][0]["message"]["content"][0]["text"]
    print("完整响应：", result)
    return result

def main():
    # embed = yiyan_embedding()
    # print(embed)
    qwen_api("自行车")
if __name__ == '__main__':
    main()