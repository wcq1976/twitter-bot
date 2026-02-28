#!/usr/bin/env python3
"""
Twitter Cookie 发推脚本 - 从 tweets.json 读取内容
"""
import os
import json
import requests
from datetime import datetime, timedelta

AUTH_TOKEN = os.environ.get('AUTH_TOKEN', '')
CT0 = os.environ.get('CT0', '')

def tweet(text):
    url = "https://api.x.com/1.1/statuses/update.json"
    
    headers = {
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF%3D%3D',
        'x-csrf-token': CT0,
        'cookie': f'auth_token={AUTH_TOKEN}; ct0={CT0};',
    }
    
    resp = requests.post(url, data={'status': text}, headers=headers)
    print(resp.text)
    return resp.status_code == 200

def get_today_tweets():
    """获取今天要发的推文"""
    try:
        with open('tweets.json', 'r') as f:
            data = json.load(f)
        
        # 获取今天日期
        today = datetime.utcnow() + timedelta(hours=8)  # 北京时间
        date_str = today.strftime('%Y-%m-%d')
        
        return data.get(date_str, [])
    except Exception as e:
        print(f"读取 tweets.json 失败: {e}")
        return []

if __name__ == "__main__":
    tweets = get_today_tweets()
    
    if not tweets:
        print("今天没有要发的推文")
        sys.exit(0)
    
    print(f"今天有 {len(tweets)} 条推文要发送")
    
    for i, text in enumerate(tweets, 1):
        print(f"\n发送第 {i} 条: {text}")
        tweet(text)
