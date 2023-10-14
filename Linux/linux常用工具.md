注意，我用的是ubuntu22，其他系统命令有差别，找对应系统的命令

- `sudo apt update`

- `sudo apt upgrade`



# 显示目录结构tree

`sudo apt install tree`



# c++相关

- GNU 编辑器集合，GNU 调试器，和其他编译软件所必需的开发库和工具。

  ~~~bash
  sudo apt install build-essential 
  # 这个命令将会安装一系列软件包，包括gcc,g++,和make。但是不包括gdb
  ~~~

- gdb调试工具

  ~~~bash
  sudo apt install gdb
  ~~~

- 使用man手册的方式，能大大加快开发速度，可能安装的时候有些安装不完整，下面结合网络上搜索信息进行补充：

  ~~~bash
  sudo apt-get install manpages
  sudo apt-get install manpages-dev
  sudo apt-get install manpages-posix
  sudo apt-get install manpages-posix-dev
  ~~~

  ~~~bash
  manpages 包含 GNU/Linux 的基本操作
  manpages-dev 包含 GNU/Linux 的基本操作API
  manpages-posix 包含 POSIX 所定义公用程序的方法
  manpages-posix-dev 包含 POSIX 的 header files 和 library calls 的用法
  ~~~

  **安装The Linux man-pages project最新文档方便查找：(推荐，包含 linux programmer's manual)**

  下载：[https://www.kernel.org/doc/man-pages/](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fwww.kernel.org%2Fdoc%2Fman-pages%2F) 

  [https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/](https://cloud.tencent.com/developer/tools/blog-entry?target=https%3A%2F%2Fmirrors.edge.kernel.org%2Fpub%2Flinux%2Fdocs%2Fman-pages%2F)

  最新安装包：https://mirrors.edge.kernel.org/pub/linux/docs/man-pages/man-pages-5.04.tar.gz 

  解压：tar xvzf packages.tar.gz 

  安装：make install 

  更新whatis [数据库](https://cloud.tencent.com/solution/database?from_column=20065&from=20065)： mandb 命令，进行更新；

- 

  