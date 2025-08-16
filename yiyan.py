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

def yiyan_api(message,use4=False):
    API_Key = Config.API_Key
    if use4:
        url = "https://qianfan.baidubce.com/v2/chat/completions"
    else:

        url = "https://qianfan.baidubce.com/v2/chat/completions"
    payload = json.dumps({
        "model": "qianfan-8b",
        "messages": [
            {
                "role": "user",
                "content": message
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + API_Key
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print("返回的内容是",response.text)
    try:
        result = json.loads(response[0].message.content)
    except Exception as e:
        print(response.text)
    #     print("API请求异常：", e)
        result = "error"
    # print(result)
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

    result = json.loads(response.text)["data"][0]["embedding"]
    return result

def main():
    embed = yiyan_embedding()
    print(embed)
if __name__ == '__main__':
    main()