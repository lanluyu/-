niwo爬虫项目说明文档
==
介绍
 - 
niwo是一个基于Scrapy的贴吧帖子信息爬虫，爬取了你我社区的所有帖子主题及链接信息。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

### 其它
在爬取你我交流的社区时，该网站用到的唯一防爬手段就是检测请求的User-Agent。直接在Scrapy中添加一个随机切换User-Agent的中间件即可。分析其网页构成时，发现前两页的最后回复时间和后面的最后回复时间的在HTML结构中不一样，所以先爬取前两页，再改变XPATH爬取剩余的页面。为了防止对该网站服务器造成压力，设置了5S的延迟，总共花了40分钟左右的时间爬取完成。

爬取结果
-
在你我社区贴吧中总共获取了8121条贴吧主题信息。每条信息中还包括了该主题的浏览人数和帖子的链接。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![贴吧信息截图](https://github.com/lanluyu/-/blob/master/%E4%BD%A0%E6%88%91%E9%87%91%E8%9E%8D%E7%A4%BE%E5%8C%BA%E5%B8%96%E5%AD%90.PNG)
