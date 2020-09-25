import urllib.request
from bs4 import BeautifulSoup
import re
import xlwt


def get_html_text(url):
    """
    # 1. 下载网页源码，并解码
    :param url:
    :return:
    """
    # 准备请求参数
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    # 封装请求
    request = urllib.request.Request(url=url, headers=headers)

    # 发送请，获取响应
    response = urllib.request.urlopen(request)

    # 提取源码，并解码
    html_doc = response.read().decode('utf-8')

    # 返回值
    return html_doc


def get_data_lst(html_doc, data_lst):
    """
    # 2. 解析网页源码，并提取所以需要采集的数据
    :param html_doc:
    :param data_lst:
    :return: data_lst 数据列表
    """
    soup = BeautifulSoup(html_doc, 'html.parser')
    items = soup.find_all('div', class_='item')

    for item in items:
        # 电影链接
        movie_link = re.findall(r'<a href="(.+)">', str(item))

        # 图片链接
        img_link = re.findall(r"""<img alt=.+ class="" src="(.+)" width="100"/>""", str(item), re.S)

        # 中文名称
        movie_name_lst = re.findall(r'<span class="title">(.+)</span>', str(item))
        chinese_name = movie_name_lst[0]

        # 外语名称
        if len(movie_name_lst) == 2:
            foreign_name = movie_name_lst[1]
        else:
            foreign_name = None

        # 电影概况
        general = re.findall(r'<p class="">(.+?)</p>', str(item), re.S)

        # 评分
        rate = re.findall(r'<span class="rating_num" property="v:average">(.+)</span>', str(item))

        # 评价人
        statistics = re.findall(r'<span>(.+)人评价</span>', str(item))

        # 相关信息
        other_info = re.findall(r'<span class="inq">(.+)</span>', str(item))

        # 提取存储在一个列表中，整合为一条记录
        data = [movie_link, img_link, chinese_name, foreign_name, general, rate, statistics, other_info]

        # 将整合后的每一条记录逐一存储到一个列表中
        data_lst.append(data)

    # 返回值
    return data_lst


def save_data(data_lst, save_path):
    """
    # 3. 保存数据到excel
    :param save_path:
    :param data_lst:
    :return: 将数据保持到指定的 excel中
    """
    # create workbook obj
    workbook = xlwt.Workbook(encoding='utf-8')

    # create sheet
    worksheet = workbook.add_sheet('top 250')

    # write
        # i) 写入目录
    column = ("电影链接", "图片链接", "中文名称", "外语名称", "电影概况", "评分", "评价人", "相关信息")
    for i in range(0, 8):
        worksheet.write(0, i, column[i])

        # ii) 写入数据
    for i in range(0, len(data_lst)):
        data = data_lst[i]
        for j in range(0, 8):
            worksheet.write(i+1, j, data[j])

    # save
    workbook.save(save_path)


def main():
    if __name__ == "__main__":
        data_lst = []
        for i in range(0, 10):
            url = "https://movie.douban.com/top250?start={}".format(i*25)
            html_doc = get_html_text(url)
            data_lst = get_data_lst(html_doc, data_lst)
        save_path = "../Data/top_250.xls"
        save_data(data_lst, save_path)

main()