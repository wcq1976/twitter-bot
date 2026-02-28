#!/usr/bin/env python3
"""
Twitter Cookie 发推脚本
"""
import os
import sys
import requests

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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python tweet.py '推文内容'")
        sys.exit(1)
    
    text = sys.argv[1]
    tweet(text)
