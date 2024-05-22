import requests
import pandas as pd

def fetch_company_and_products(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # 检查是否成功获取响应
        data = response.json()  # 将响应内容解析为JSON格式
        
        if data['code'] == 1:
            companies = data['data']
            # 创建一个空的列表，用于存储公司和产品信息
            records = []
            for company in companies:
                company_name = company['companyname']
                products = company.get('productlist', [])
                for product in products:
                    product_name = product['productname']
                    # 将公司名称和产品名称添加到记录列表中
                    records.append({'公司名称': company_name, '产品名称': product_name})
            
            # 将记录列表转换为pandas DataFrame
            df = pd.DataFrame(records)
            
            # 设置pandas显示选项以展示全部内容而不进行缩略
            pd.set_option('display.max_rows', None)
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_colwidth', None)
            pd.set_option('display.expand_frame_repr', False)
            
            # 打印DataFrame以表格格式显示
            print(df)
        else:
            print("API返回错误信息:", data['msg'])
    except requests.exceptions.RequestException as e:
        print(f"请求发生错误: {e}")

# 调用函数并传入API URL
api_url = "https://card.chtf.org.cn/chtf/cn/GetCompany-682?pageindex=1&limit=500&gb=&keywords="
fetch_company_and_products(api_url)
