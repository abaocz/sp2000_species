# 中国生物物种名录

sp2000爬虫所有物种

**该爬虫仅供学习使用**

## 文件介绍

- `test_allURL.py`：爬取所有的物种的URL放入file.txt中
- `test_kcURL.py`：爬取所有的昆虫的URL放入file.txt中
- `test_爬取.py`：读取file.txt中的URL，然后爬取。
- `Thread_爬取.py`：读取file.txt中的URL，然后多线程爬取。文件里面的num_threads表示线程数。

~~~shell
#test_allURL.py和test_KcURL.py里面的参数指定。
#用户代理
UserAgent=""
#里面参数加上JSESSIONID
Cookie=""
#csrf在html中搜索csrf获取
csrf_token=""
~~~
