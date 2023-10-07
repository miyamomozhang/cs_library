# 普通用户和root用户、根目录和家目录

~~~
/：根目录，Linux系统的根目录，最上层目录

~：家目录，每个用户的家目录，路径：/home/user_name

$：普通用户

#：root用户
~~~


ubuntu登录后，默认是普通用户权限。新安装的ubuntu是没有设置root用户的密码的，我们只是建了一个普通用户。

## 查看用户

很详细，要的基本都有，看Linux中国这篇文档 https://zhuanlan.zhihu.com/p/41161408

三种方式： `/etc/passwd` 文件，`getent` 命令，`compgen`

查看系统中所有用户：`grep bash /etc/passwd`

查看当前用户：`w`    `who`   `users`

# 普通用户切换到root用户

1. `su`，按照提示输入root密码

2. `sudo su`，按照提示输入root密码 (这个命令一般不需要输root密码就可以成功)。

3. `su root`，按照提示输入root密码

# root用户切换到普通用户

1. `su username ` ( username 是安装ubuntu时候的用户名)

2. `exit`

3. Ctrl+D

# 给root用户设定密码 

`sudo passwd root` 根据提示一步一步来。


禁用和启用root登录

执行sudo passwd -l root即可（只是禁用root，但是root密码还保存着），再执行su root发现认证失败，(但是sudo su命令仍可进入root模式下)。

要再次启动root登录，执行sudo passwd -u root 即。
