# DanmuSpider
## 简介
一键获取热点事件的所有弹幕

## 声明
本接口并没有加密参数，但并不意味着可以随意频繁调用
调用接口获取信息只是跳过了手动去网页复制粘贴的过程
而且cookie中是有个人信息的，频繁调用接口造成不好影响是会被追究责任的
所以合理运用此工具，仅供学习交流

## 使用步骤
只需要复制粘贴一下cookie，然后就可以自动

把cookie复制粘贴在cookie.txt文件中，隐私考虑可以新建mycookie.txt文件在其中粘贴cookie

web页面
<br />
https://search.bilibili.com/all?vt=67184772&keyword=315%E6%99%9A%E4%BC%9A&from_source=webtop_search&spm_id_from=333.1007&search_source=5&page=2&o=24
<br />
获取videolist与aid
<br />
https://api.bilibili.com/x/web-interface/wbi/search/type?search_type=video&keyword=315%E6%99%9A%E4%BC%9A&page_size=50
<br />
获取oid
<br />
https://api.bilibili.com/x/web-interface/view?aid=1051819621
<br />
获取弹幕
<br />
https://api.bilibili.com/x/v1/dm/list.so?oid=1471465268


## TODO
GUI页面，让不会python的同学也可以使用软件
视频投币过100立马赶工出来！