# .gitignore文件模板

gitignore文件是有模板的，我们不需要自己写，如Python的gitignore文件：
https://github.com/github/gitignore/blob/main/Python.gitignore

上面这个仓库上还有其他语言的.gitignore文件模板可供参考

或者可以参考下面这个：https://www.toptal.com/developers/gitignore

# .gitignore规范

.gitignore文件用于忽略文件，规范如下：

- 所有空行或者以注释符号 ＃ 开头的行都会被 Git 忽略
- 可以使用标准的 glob 模式匹配
- 匹配模式最后跟反斜杠（/）说明要忽略的是目录
- 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号（!）取反
- 第一个 / 会匹配路径的根目录，举个栗子，”/*.html”会匹配”index.html”，而不是”d/index.html”。
- 通配符 * 匹配任意个任意字符，? 匹配一个任意字符。需要注意的是通配符不会匹配文件路径中的 /，举个栗子，”d/*.html”会匹配”d/index.html”，但不会匹配”d/a/b/c/index.html”。
- 两个连续的星号 **有特殊含义：
    - 以 **/ 开头表示匹配所有的文件夹，例如 **/test.md 匹配所有的test.md文件。
    - 以 /** 结尾表示匹配文件夹内所有内容，例如 a/** 匹配文件夹a中所有内容。
    - 连续星号 ** 前后分别被 / 夹住表示匹配0或者多层文件夹，例如 a/**/b 匹配到 a/b 、a/x/b 、a/x/y/b 等。
- 前缀 ! 的模式表示如果前面匹配到被忽略，则重新添加回来。如果匹配到的父文件夹还是忽略状态，该文件还是保持忽略状态。如果路径名第一个字符为 ! ，则需要在前面增加 \ 进行转义。

# mac的.gitignore文件

参考github官方文档：https://docs.github.com/en/get-started/getting-started-with-git/ignoring-files

中文版：https://docs.github.com/zh/get-started/getting-started-with-git/ignoring-files

.DS_Store 是用于存放目录自定义属性（如图表、位置属性）等元数据信息的系统文件，由 Finder 自动创建。虽然所有 . 开头的文件/文件夹默认隐藏（可以使用 Command + Shift + . 显示所有隐藏文件），平时我们看不见，也不影响使用，但是 Git 仍会将其记录下来，即便我只是在同目录下移动文件。所以为了防止某些信息不经意间泄露出来，建议使用某些手段使 Git 忽略 .DS_Store 文件。

## 全局配置

- 打开终端，在某一个位置创建 .gitignore_global 文件（建议在当前用户目录下）：
    ~~~
    touch ~/.gitignore_global
    ~~~
    打开文件 vi ~/.gitconfig
    或open ~/.gitignore_global
    ~~~
    .DS_Store
    **/.DS_Store
    .DS_Store?
    ~~~

- 对git进行全局设置，让git忽略.gitignore_global中的所有文件：
    ~~~
    git config --global core.excludesfile ~/.gitignore_global
    ~~~


## 单个项目配置

针对.DS_Store文件，在git工程文件夹中新建.gitignore文件，在文件中设置：
~~~
.DS_Store
**/.DS_Store
.DS_Store?
~~~

## 对于已经提交的

希望git能够忽略，但同时并不会删除本地文件，需要在控制台输入以下命令：
~~~
git rm -r --cached $file_path
~~~

## 批量移除已有的 .DS_Store

即便后续不会再记录，仓库中的 .DS_Store 都还在，需要手动删除。

终端进入仓库目录，输入：
~~~
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
~~~
这样就删除了所有该仓库的 .DS_Store 。重新提交推送git push即可。


# .gitignore文件补充

自己不能或者暂时不想上传github上，项目中确实需要用到的，在.gitignore文件中注明，我自己会在学习的时候遇到一些没有解决的问题或者坑，通常会创建一个NotSettled文件夹，在上面创建markdown文件进行记录，有些问题并不能马上解决，也避免过后会忘，采用这种方式记录，重要工作完成之后再来解决，解决完成之后我会放到 Notes 文件夹记录解决的方案。
