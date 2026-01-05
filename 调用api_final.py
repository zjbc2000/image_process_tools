import requests
import json

# API端点
url = "http://127.0.0.1:5000/api/scripts/56/run"

# 准备参数（支持列表、布尔值等复杂类型）
params = {
    "minio_endpoint": "127.0.0.1",
    "crop_coordinates": [(100, 100, 200, 400), (300, 200, 800, 600), (100, 500, 400, 900)],
    "forbid_redirect": True,
    "auto_infer_from_url": True,
    "preflight_minio_health": True,
    "cleanup_downloaded": True,
    "timeout": 120
}

# 将参数转换为JSON字符串
data = json.dumps(params)

# 发送POST请求
response = requests.post(url, data=data, headers={"Content-Type": "application/json"})

# 打印响应
print(f"状态码: {response.status_code}")
print(f"响应内容: {response.text}")

# 如果响应是JSON，解析并打印
try:
    result = response.json()
    print(f"\n解析后的响应:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # 提取minio_url列表，按index排序
    if "return_value" in result and "results" in result["return_value"]:
        results = result["return_value"]["results"]
        # 按index排序
        sorted_results = sorted(results, key=lambda x: x["index"])
        # 提取minio_url组成列表
        minio_urls = [item["minio_url"] for item in sorted_results]
        
        print(f"\n📎 MinIO URL列表（按index排序）:")
        for i, url in enumerate(minio_urls, 1):
            print(f"   [{i}] {url}")
        
        print(f"\n📋 MinIO URL列表（Python格式）:")
        print(minio_urls)
except:
    pass

