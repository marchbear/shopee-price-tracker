import requests

url = "https://shopee.tw/-VT-BHA-AHA-CICA-%E5%8E%BB%E8%A7%92%E8%B3%AA%E5%8C%96%E5%A6%9D%E6%B0%B4%E6%A3%89%E7%89%87-60%E7%89%87%E5%85%A5-%E5%AE%98%E6%96%B9%E6%97%97%E8%89%A6%E5%BA%97--i.229003803.12042246873"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("狀態碼：", response.status_code)
print("網頁長度：", len(response.text))

if response.status_code == 200:
    print("成功取得蝦皮商品頁面！")
else:
    print("取得商品頁面失敗。")
