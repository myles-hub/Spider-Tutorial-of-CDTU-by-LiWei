import urllib.request
from bs4 import BeautifulSoup
import xlwt
from tqdm import tqdm


def get_html_doc(url):
    """
    1. 下载网页源码
    :param:
    :return: 网页内容
    """
    # 准备请求参数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    # 封装请求参数
    request = urllib.request.Request(url=url, headers=headers)

    # 发送请求，获取响应
    response = urllib.request.urlopen(request)

    # 提取内容，并解码
    content = response.read().decode()

    return content


def get_data_lst(html_doc, data_lst):
    """
    2. 解析html_doc文档内容，并提取所需信息
    :return: data_lst
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    item_lst = soup.find_all('div', class_='item')

    for item in item_lst:
        # 电影链接
        movie_link = item.find('a').get('href')

        # 图片链接
        img_link = item.find('img').get('src')

        # 中文名称
        movie_of_name_lst = item.find_all('span', class_="title")
        chinese_name = movie_of_name_lst[0].get_text()

        # 外语名称
        if len(movie_of_name_lst) == 2:
            foreign_name = movie_of_name_lst[1].get_text()
        else:
            foreign_name = None

        # 电影概况
        general = item.find('p').get_text()

        # 评分
        star = item.find('div', class_='star')
        span_lst = star.find_all('span')
        rate = span_lst[1].get_text()

        # 评价人
        evaluator = span_lst[3].get_text()

        # 相关信息
        if item.find('span', class_="inq"):
            other_info = item.find('span', class_="inq").get_text()
        else:
            other_info = None

        lst = [movie_link, img_link, chinese_name, foreign_name, general, rate, evaluator, other_info]
        data_lst.append(lst)

    return data_lst


def save_data(data_lst):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet("Top250")
    column = ("电影链接", "图片链接", "中文名称", "外语名称", "电影概况", "评分", "评价人", "相关信息")

    # 写入目录
    for i in range(0, 8):
        worksheet.write(0, i, column[i])

    # 将数据写入excel
    # for i in range(0, len(data_lst)):
    #     data = data_lst[i]
    #     for j in range(0, 8):
    #         worksheet.write(i+1, j, data[j])

    i = 1
    for data in data_lst:
        for j in range(len(data)):
            worksheet.write(i, j, data[j])
        i += 1

    # 保存都文件
    workbook.save(r"C:\Users\myles\Desktop\top25_of_movie.xls")


def main():
    data_lst = []
    if __name__ == "__main__":
        for i in tqdm(range(0, 25), "Top250 内容下载进度"):
            url = "https://movie.douban.com/top250?start={}".format(25 * i)
            html_doc = get_html_doc(url)
            data_lst = get_data_lst(html_doc, data_lst)
            save_data(data_lst)


main()
