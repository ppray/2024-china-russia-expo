import requests
from bs4 import BeautifulSoup

# 基础URL
base_url = 'https://card.chtf.org.cn/chtf/cn/jyqy-{}-5.html'

# 循环遍历页面1到6
for i in range(1, 7):
    # 构建完整的页面URL
    url = base_url.format(i)
    
    # 获取页面内容
    response = requests.get(url)
    response.encoding = 'utf-8'  # 确保正确的编码
    
    # 检查请求是否成功
    if response.status_code == 200:
        html_content = response.text
        
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # 找到所有交易条目
        items = soup.select('.list2 ul li')
        
        for item in items:
            # 获取签约双方信息
            parties = item.select_one('.text p').text.strip()
            
            # 获取交易金额
            amount = item.select_one('.jine .num').text.strip()
            
            # 打印签约双方和交易金额
            print(f"{parties} - 交易金额: {amount} 亿人民币")
    else:
        print(f"Failed to retrieve the page {url}. Status code: {response.status_code}")
