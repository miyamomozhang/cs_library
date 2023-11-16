# .文件模板

文件网上有很多模板，我们不太需要自己写，如Python的文件：
https://github.com/github//blob/main/Python.

上面这个仓库上还有其他很多.文件模板可供参考，我看了没找到Django之类的，只看到了Python的

或者可以参考下面这个：https://www.toptal.com/developers/gitignore ，这个网站找到的比较多

# .规范

一般先找模板套，但是实际运用上，我们很多时候还是需要改的，需要遵守规范。

我自己的仓库，本地我可能会用到一些记录的文件，不太想要发布到网上，仅仅是给自己学习做一个参考，记录暂时没解决的难点和坑，包括一些不能理解的疑问，完全没有梳理，像记草稿一样，没有什么逻辑，不太适合发布。

.文件用于忽略文件，规范如下：（glob模式匹配）

官方详细版：https://git-scm.com/docs/

| .                                                   | Git                   |
| ------------------------------------------------------------ | --------------------- |
| 空行或注释（#）                                              | 忽略空行和注释        |
| 有斜杠 /：目录，无：文件                                     | 不提交相应文件/文件夹 |
| 使用标准的glob模式匹配（ [glob Wikipedia](https://en.wikipedia.org/wiki/Glob_(programming))） |                       |
| 通配符 * ：0/多个字符                                        |                       |
| 通配符 ？：1个字符                                           |                       |
| `**`：<br />`dir/** `：匹配dir文件夹所有内容<br />`dir1/**/dirn` ：匹配0或者多层文件夹 |                       |
| 前缀 !（取反） 的模式表示如果前面匹配到被忽略，则重新添加回来。<br />如果匹配到的父文件夹还是忽略状态，该文件还是保持忽略状态。<br />如果路径名第一个字符为 ! ，则需要在前面增加 \ 进行转义。<br />（补充：win的路径名是反斜杠\，在前面加一个\转义） |                       |

# mac的.文件

参考github官方文档：https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files

中文版：https://docs.github.com/zh/get-started/getting-started-with-git/ignoring-files

.DS_Store 是用于存放目录自定义属性（如图表、位置属性）等元数据信息的系统文件，由 Finder 自动创建。虽然所有 . 开头的文件/文件夹默认隐藏（可以使用 Command + Shift + . 显示所有隐藏文件），平时我们看不见，也不影响使用，但是 Git 仍会将其记录下来，即便我只是在同目录下移动文件。所以为了防止某些信息不经意间泄露出来，建议使用某些手段使 Git 忽略 .DS_Store 文件。

## 全局配置

- 打开终端，在某一个位置创建 ._global 文件（建议在当前用户目录下）：
    ~~~
    touch ~/._global
    ~~~
    打开文件 vi ~/.gitconfig
    或open ~/._global
    ~~~
    .DS_Store
    **/.DS_Store
    .DS_Store?
    ~~~

- 对git进行全局设置，让git忽略._global中的所有文件：
    ~~~
    git config --global core.excludesfile ~/._global
    ~~~


## 单个项目配置

针对.DS_Store文件，项目文件夹的.文件设置：
~~~
.DS_Store
**/.DS_Store
.DS_Store?
~~~

## 对于已经提交的

希望git忽略，本地保留，终端输入：
~~~
git pull origin main
git rm -r --cached $file_path
~~~

## 批量移除已有的 .DS_Store

即便后续不会再记录，仓库中的 .DS_Store 都还在，需要手动删除。

终端进入仓库目录，输入：
~~~
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
~~~
这样就删除了所有该仓库的 .DS_Store 。重新提交推送git push即可。


# .文件补充

自己不能或者暂时不想上传github上，项目中确实需要用到的，在.文件中注明，我自己会在学习的时候遇到一些没有解决的问题或者坑，通常会创建一个NotSettled文件夹，在上面创建markdown文件进行记录，有些问题并不能马上解决，也避免过后会忘，采用这种方式记录，重要工作完成之后再来解决，解决完成之后我会放到 Notes 文件夹记录解决的方案。
