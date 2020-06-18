# -*- coding:utf-8 -*-
from pyecharts.custom.page import Page
from pyecharts import Graph
from pyecharts import Style
import math
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
def color_choose(number):
    if number > 200000:
        color = 'rgba(255,102,102,0.8)'
    elif number > 20000:
        color = 'rgba(255,204,0,0.8)'
    elif number > 2000:
        color = 'rgba(102,153,51,0.8)'
    elif number > 200:
        color = 'rgba(51,153,204,0.8)'
    elif number > 20:
        color = 'rgba(153,50,204,0.8)'
    elif number > 2:
        color = 'rgba(205,133,63,0.8)'
    else:
        color = 'rgba(204,204,204,0.8)'
    return color

if __name__ == "__main__":

    ktv=open('D:\PY\GraphX\handle\ktv.txt','r',encoding='utf-8')
    list1 = ktv.read().split("\n")
    list0=[]
    count = 0
    for i in list1:
        count += 1
        if count == 1:
            continue
        list0.append(i)

    node = list()
    node.append(({'name': 0, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 1, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 2, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 3, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 4, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 5, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 6, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 7, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 8, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))
    node.append(({'name': 9, 'symbolSize': 5, 'itemStyle': {'color': 'rgba(204,204,204,0.8)'}}))

    link = list()

    mcount=0

    for j in list0:
        mcount+=1
        view = eval(j)[2]
        size = int(math.sqrt(view) * 2)
        this_color = color_choose(size)
        node.append(({'name': eval(j)[1]+str(mcount), 'symbolSize': 10, 'itemStyle': {'color': this_color}}))
        link.append({'source': eval(j)[1]+str(mcount), 'target': eval(j)[0]})

    style = Style(
        title_color="#fff",
        title_pos="center",
        width=2760,
        height=1440,
        background_color='#404a59'

    )
    for m in node:
        print(m)
    print(len(node))
    print(len(link))

    page = Page()
    chart = Graph("聚类图", **style.init_style)
    chart.add("", node, link)
    page.add(chart)
    page.render()