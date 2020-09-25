import urllib.request
from bs4 import BeautifulSoup
import re
import sqlite3
from tqdm import tqdm


# 一、下载网页源码
def get_html_doc(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    html_doc = response.read().decode('utf-8')
    return html_doc


# 二、解析并提取所需数据

def get_data_lst(html_doc, data_lst):
    soup = BeautifulSoup(html_doc, 'html.parser')
    tag_items = soup.find_all('div', class_='item')

    for item in tag_items:
        # 电影链接
        movie_link = item.find('a').get('href')
        # 图片链接
        img_link = item.find('img').get('src')
        # 中文名称
        movie_names = item.find_all('span', class_='title')
        chinese_name = movie_names[0].get_text()
        # 外语名称
        if len(movie_names) == 2:
            foreign_name = movie_names[1].get_text()
        else:
            foreign_name = None
        # 电影概况
        general_info = item.find('p', class_='').get_text()
        # 电影评分
        rate = item.find('span', class_="rating_num").get_text()
        # 评价统计
        count = re.findall(r'<span>(\d+)\w+</span>', str(item))[0]
        # 一句话
        if item.find('span', class_="inq"):
            desc = item.find('span', class_="inq").get_text()
        else:
            desc = None

        # 列表收集数据
        data = [movie_link, img_link, chinese_name, foreign_name, general_info, count, desc]
        data_lst.append(data)

    return data_lst

# 三、 保存数据

def save_data(db_path, data_lst):
    # create db in RAM
    conn = sqlite3.connect(db_path)
    print("Opened Database Successfully.")

    # create cursor
    cursor = conn.cursor()

    # execute sql
    sql_create_table = """
        CREATE TABLE MOVIE (
        ID INT PRIMARY KEY NOT NULL,
        movie_link CHAR(100),
        img_link CHAR(100),
        chinese_name CHAR(50),
        foreign_name CHAR(50),
        general_info CHAR(200),
        count INT,
        desc CHAR(100)
        )
    """

    cursor.execute(sql_create_table)
    print("Create table Successfully.")

    # insert data
    for data in data_lst:
        row = """{0},'{1}','{2}','{3}',"{4}","{5}",{6},"{7}" """.format(data_lst.index(data), data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        print(row)

        sql_insert = """
            INSERT INTO MOVIE (ID, movie_link, img_link, chinese_name, foreign_name, general_info, count, desc)
            VALUES ({})""".format(row)

        # print(sql_insert)
        cursor.execute(sql_insert)
        print(">>> Insert Successfully： {}".format(data_lst.index(data)))

    conn.commit()
    conn.close()


def main():
    if __name__ == '__main__':

        data_lst = []
        for i in tqdm(range(0, 25), "Top250 数据抓取进度"):
            url = "https://movie.douban.com/top250?start={}".format(i*25)
            html_doc = get_html_doc(url)
            data_lst = get_data_lst(html_doc, data_lst)
        save_data('./top250.db', data_lst)


# main()





# +++++++++++++++++++++ 数据查询实例 ++++++++++++++++++++
# Create a db in RAM
conn = sqlite3.connect('top250_8.db')
print("Opened DataBase Successfully.")

# Create a cursor
cursor = conn.cursor()

# Execute sql
sql = """
    select * from movie;
    """

rows_lst = cursor.execute(sql)


# for row in rows_lst:
#     print("{0}\t|{1}\t|{2}\t|{3}\t|{4}\t|{5}\t|{6}\t|{7}\t".format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

for row in rows_lst:
    print("{0}\t|{1}\t|{2}\t|{3}\t".format(row[0]+1, row[3], row[4], row[7]))
