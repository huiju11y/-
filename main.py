from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载配置文件
load_dotenv()

# 初始化MiniMax客户端
client = OpenAI(
    api_key=os.getenv("MINIMAX_API_KEY"),
    base_url="https://api.minimax.chat/v1",
)

# 发送请求
response = client.chat.completions.create(
    model="abab6.5-chat",
    messages=[
        {"role": "user", "content": "你好，介绍一下自己"}
    ]
)

# 打印回复
print("AI回复：", response.choices[0].message.content)