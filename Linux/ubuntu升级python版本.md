1. 安装Python 3.11 版本
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.11
2. 设置默认的Python版本
$ python3 --version
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
$ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.11 2
$ sudo update-alternatives --config python3
$ python3 --version