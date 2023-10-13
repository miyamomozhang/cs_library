

报错：`unable to locate package XXXXXXXXX`

原因：软件源没有更新

解决：`sudo apt-get update`

`sudo apt-get update` ：访问源列表里的每个网址，并读取软件列表的最新源，然后保存在本地Linux。【更新的是软件源，Linux当前安装的软件不会自动更新】



注意区分`sudo apt-get upgrade` ：Linux当前安装的软件会自动更新



apt-get常用命令如下:

- apt-cache search package 搜索包
- apt-cache show package 获取包的相关信息，如说明、大小、版本等
- sudo apt-get install package 安装包
- sudo apt-get install package - - reinstall 重新安装包
- sudo apt-get -f install 修复安装"-f = ——fix-missing"
- sudo apt-get remove package 删除包
- sudo apt-get remove package - - purge 删除包，包括删除配置文件等
- sudo apt-get update 更新源
- sudo apt-get upgrade 更新已安装的包
- sudo apt-get dist-upgrade 升级系统
- sudo apt-get dselect-upgrade 使用 dselect 升级
- apt-cache depends package 了解使用依赖
- apt-cache rdepends package 是查看该包被哪些包依赖
- sudo apt-get build-dep package 安装相关的编译环境
- apt-get source package 下载该包的源代码
- sudo apt-get clean && sudo apt-get autoclean 清理无用的包
- sudo apt-get check 检查是否有损坏的依赖

