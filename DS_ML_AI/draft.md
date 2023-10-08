# 神经网络的训练技术

反向传播、弹性传播、量化共轭梯度 (SCG)、 曼哈顿更新规则传播

https://zhuanlan.zhihu.com/p/48982978

tensor 张量  https://blog.csdn.net/u010995990/article/details/80093252


## 机器学习数据集

https://www.zhihu.com/question/342295029/answer/2928765090

### 通用综合数据集

1. **UCI机器学习库**
   链接：[http://archive.ics.uci.edu/ml/datasets.php](https://link.zhihu.com/?target=http%3A//archive.ics.uci.edu/ml/datasets.php)
   UCI机器学习库是[加州大学欧文分校](https://www.zhihu.com/search?q=加州大学欧文分校&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})(University of CaliforniaIrvine)提出的用于机器学习的[数据库](https://www.zhihu.com/search?q=数据库&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})，这个数据库共有622个数据集，其数目还在不断增加，UCI数据集是一个常用的标准[测试数据](https://www.zhihu.com/search?q=测试数据&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})集。虽然这里的数据集是[用户贡献](https://www.zhihu.com/search?q=用户贡献&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的，因此清洁度不一，但绝大多数都是干净的。

![img](https://pic2.zhimg.com/80/v2-0c2a4d41f063cb787ea9a742257b75e3_1440w.webp)

1. **Kaggle**

链接：[https://www.kaggle.com/datasets](https://link.zhihu.com/?target=https%3A//www.kaggle.com/datasets)

一个包含各种外部贡献数据集的数据科学网站，其中包括了各种外部贡献的机器学习数据集，从健康到运动，再到食物、旅行、教育等等。每天都有无数爱好者在该平台更新数据，虽然说数据质量参差不齐，但是所有数据都是免费的，而且还可以上传自己数据集。



### [公共政府数据集](https://www.zhihu.com/search?q=公共政府数据集&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})

1. **国家统计局**
   链接：[http://www.stats.gov.cn/](https://link.zhihu.com/?target=http%3A//www.stats.gov.cn/)
   国家统计局的官方网站，上面汇集了海量的全国各级政府各年度的国民经济和社会发展统计信息，用户还可以在上面找到统计年鉴、阶段发展数据、统计分析、[经济新闻](https://www.zhihu.com/search?q=经济新闻&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})、主要[统计指标](https://www.zhihu.com/search?q=统计指标&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})排行等。
2. **[http://Data.gov](https://link.zhihu.com/?target=http%3A//Data.gov)**
   链接：[https://data.gov/](https://link.zhihu.com/?target=https%3A//data.gov/)
   [美国政府](https://www.zhihu.com/search?q=美国政府&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})公开数据之家，该站点包含335,221数据集，该数据集包含气候、教育、能源、金融和更多其他领域的数据。
3. **IES NCES**
   链接：[https://nces.ed.gov/](https://link.zhihu.com/?target=https%3A//nces.ed.gov/)
   美国和世界各地教育机构和教育人口统计数据。
4. **Data USA**

链接：[https://datausa.io/](https://link.zhihu.com/?target=https%3A//datausa.io/)

提供美国各类数据，包含各产业的数据、各职业数据、各大学数据等，同时还提供数据下载和[可视化](https://www.zhihu.com/search?q=可视化&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})查看。

### [自然语言处理数据集](https://www.zhihu.com/search?q=自然语言处理数据集&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})

1. **Enron Email Dataset**
   链接：[https://www.cs.cmu.edu/~enron/](https://link.zhihu.com/?target=https%3A//www.cs.cmu.edu/~enron/)
   Enron Email Dataset（安然[电子邮件](https://www.zhihu.com/search?q=电子邮件&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})数据集），是由CALO项目（学习和组织的认知助手）收集和准备的数据集。包括了由[安然公司](https://www.zhihu.com/search?q=安然公司&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})约150+名员工生成的超过500000封电子邮件。
2. **Amazon Review Data (2018)**
   链接：[https://nijianmo.github.io/amazon/index.html](https://link.zhihu.com/?target=https%3A//nijianmo.github.io/amazon/index.html)
   Amazon Review Data（[亚马逊](https://www.zhihu.com/search?q=亚马逊&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})评论数据 (2018）包含1996年至2018年期间收集的2.331亿条评论。
3. **SMS Spam Collection in English**
   链接：[https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset](https://link.zhihu.com/?target=https%3A//www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
   SMS Spam Collection in English（英文[垃圾短信](https://www.zhihu.com/search?q=垃圾短信&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})收集）是一个小型数据集，包含 5574 条带有 SMS 标记的消息（英文），用于手机垃圾邮件研究，能够被标记为合法或垃圾邮件。
4. **The Blog Authorship Corpus**
   链接：[https://u.cs.biu.ac.il/~koppel/BlogCorpus.htm](https://link.zhihu.com/?target=https%3A//u.cs.biu.ac.il/~koppel/BlogCorpus.htm)
   从[http://blogger.com](https://link.zhihu.com/?target=http%3A//blogger.com)收集的681,288篇博客文章，每篇博客至少包含200个常用的[英语单词](https://www.zhihu.com/search?q=英语单词&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})。
5. **Yelp Reviews**

链接：[https://www.yelp.com/dataset](https://link.zhihu.com/?target=https%3A//www.yelp.com/dataset)

Yelp Reviews（Yelp评论）是一个[开放数据](https://www.zhihu.com/search?q=开放数据&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})集，包含超过600万+条评论和20万+张图片，可用于个人和学术目的的用户评论、[商业信息](https://www.zhihu.com/search?q=商业信息&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})和图像。

### [视觉图像数据集](https://www.zhihu.com/search?q=视觉图像数据集&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})

1. **Labelme**
   链接：[http://labelme.csail.mit.edu/Release3.0/browserTools/php/dataset.php](https://link.zhihu.com/?target=http%3A//labelme.csail.mit.edu/Release3.0/browserTools/php/dataset.php)
   Labelme是[麻省理工](https://www.zhihu.com/search?q=麻省理工&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})（MIT）的[计算机科学](https://www.zhihu.com/search?q=计算机科学&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})和人工智能[实验室](https://www.zhihu.com/search?q=实验室&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})（CSAIL）研发的图像[标注工具](https://www.zhihu.com/search?q=标注工具&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})，人们可以使用该工具创建定制化标注任务或执行图像标注，项目[源代码](https://www.zhihu.com/search?q=源代码&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})已经开源。
2. **ImageNet**
   链接：[https://image-net.org/download.php](https://link.zhihu.com/?target=https%3A//image-net.org/download.php)
   ImageNet 是[计算机视觉](https://www.zhihu.com/search?q=计算机视觉&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})中最受欢迎和最大的数据集之一，主要用于[深度计算机视觉](https://www.zhihu.com/search?q=深度计算机视觉&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的图像。该数据集共包含14197122个图像，该数据集跨越1000个对象类，包含1281167个训练图像、50000个[验证图像](https://www.zhihu.com/search?q=验证图像&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})和100000个测试图像。
3. **Open Images V6**
   链接：[https://storage.googleapis.com/openimages/web/index.html](https://link.zhihu.com/?target=https%3A//storage.googleapis.com/openimages/web/index.html)
   Open Images V6（[谷歌](https://www.zhihu.com/search?q=谷歌&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的开放图像数据集）图片已经超过了900万，包括了对象边界框、对象分割和标签。
4. **Indoor Scene Recognition**
   链接：[http://web.mit.edu/torralba/www/indoor.html](https://link.zhihu.com/?target=http%3A//web.mit.edu/torralba/www/indoor.html)
   Indoor Scene Recognition（[室内场景识别](https://www.zhihu.com/search?q=室内场景识别&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})）包含67个室内类别，共15620张图像，每个类别至少有100张图像。
5. **Labeled Faces in the Wild**
   链接：[http://vis-www.cs.umass.edu/lfw/](https://link.zhihu.com/?target=http%3A//vis-www.cs.umass.edu/lfw/)
   Labeled Faces in the Wild是用于训练和测试[人脸识别模型](https://www.zhihu.com/search?q=人脸识别模型&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的数据集。该数据集包含13000张[面部照片](https://www.zhihu.com/search?q=面部照片&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})，专为开发[面部识别](https://www.zhihu.com/search?q=面部识别&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})项目而设计，每张脸都标有图中人物的名字。在数据集中，1680多人有两张或多张不同的照片。
6. **Stanford Dogs Dataset**

链接：[http://vision.stanford.edu/aditya86/ImageNetDogs/](https://link.zhihu.com/?target=http%3A//vision.stanford.edu/aditya86/ImageNetDogs/)

Stanford Dogs Dataset（[斯坦福犬数据集](https://www.zhihu.com/search?q=斯坦福犬数据集&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})）包含了世界各地120种狗，共20580张图像。并通过类标签和边界框进行注释。

### 金融类数据集

1. **World Bank**
   链接：[https://data.worldbank.org/](https://link.zhihu.com/?target=https%3A//data.worldbank.org/)
   World Bank Open Data（[世界银行](https://www.zhihu.com/search?q=世界银行&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})）无需注册即可访问的来自世界银行的开放数据。涵盖了世界各地的人口统计数据和大量的经济和发展指标。该网站支持中文。
2. **IMF Data**
   链接：[https://www.imf.org/en/Data](https://link.zhihu.com/?target=https%3A//www.imf.org/en/Data)
   IMF Data是[国际货币基金组织](https://www.zhihu.com/search?q=国际货币基金组织&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})发布与国际货币基金组织贷款、汇率以及其他经济和[金融指标](https://www.zhihu.com/search?q=金融指标&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})相关的数据。
3. **Quandl**
   链接：[https://data.nasdaq.com/](https://link.zhihu.com/?target=https%3A//data.nasdaq.com/)
   Quandl拥有丰富的金融、经济和替代数据数据集，对于建立预测经济指标或股票价格的模型很有用。
4. **Financial Times Markets Data**

链接：[https://markets.ft.com/data/](https://link.zhihu.com/?target=https%3A//markets.ft.com/data/)

Financial Times Markets Data（[金融时报](https://www.zhihu.com/search?q=金融时报&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})市场数据）包含来自世界各地的[金融市场](https://www.zhihu.com/search?q=金融市场&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的最新[数据源](https://www.zhihu.com/search?q=数据源&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})，该数据集包含有关股票和股票价格、股票、货币、债券和商品表现的信息。

### 自动驾驶数据集

1. **Berkeley DeepDrive**
   链接：[https://bdd-data.berkeley.edu/](https://link.zhihu.com/?target=https%3A//bdd-data.berkeley.edu/)
   Berkeley DeepDrive是目前最大的[自动驾驶](https://www.zhihu.com/search?q=自动驾驶&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"}) AI 数据集，有10万+个在一天中不同时段、不同天气条件下共1000+个小时的驾驶体验视频。
2. **Apollo**
   链接：[https://apolloscape.auto/index.html](https://link.zhihu.com/?target=https%3A//apolloscape.auto/index.html)
   [百度](https://www.zhihu.com/search?q=百度&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"}) Apollo包括约100K图像帧、80k[激光雷达](https://www.zhihu.com/search?q=激光雷达&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})点云和1000km城市交通轨迹。数据集由不同的条件和交通密度组成，其中包括车辆、自行车和行人相互移动等场景。
3. **Cityscape Dataset**

链接：[https://www.cityscapes-dataset.com/](https://link.zhihu.com/?target=https%3A//www.cityscapes-dataset.com/)

Cityscape Dataset(城市景观数据集)包含50个不同城市的街道场景中记录的立体视频序列，是一个具有5000帧以及20000个注释帧的数据集。

### 情感分析数据集

1. **Multi-Domain Sentiment Dataset**
   链接：[https://www.cs.jhu.edu/~mdredze/datasets/sentiment/](https://link.zhihu.com/?target=https%3A//www.cs.jhu.edu/~mdredze/datasets/sentiment/)
   Multi-Domain Sentiment Dataset数据集比较老旧，其包含了来自亚马逊的正面和负面产品评论，评论包含从1到5星的评级。
2. **Stanford Sentiment Analysis**
   链接：[https://nlp.stanford.edu/sentiment/code.html](https://link.zhihu.com/?target=https%3A//nlp.stanford.edu/sentiment/code.html)
   Stanford Sentiment Analysis是一个带有情感注释的大型[电影评论](https://www.zhihu.com/search?q=电影评论&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})数据集。它包含10000多条数据。
3. **Twitter US Airline Sentiment**

链接：[https://www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment](https://link.zhihu.com/?target=https%3A//www.kaggle.com/datasets/crowdflower/twitter-airline-sentiment)

Twitter数据是从2015年2月收集的，投稿按照积极、消极和中立的推文进行分类，然后对负面原因（如“[航班延误](https://www.zhihu.com/search?q=航班延误&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})”或“服务粗鲁”）进行分类。

### [医疗数据集](https://www.zhihu.com/search?q=医疗数据集&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})

1. **Medical Information Mart for Intensive Care**
   链接：[https://mimic.mit.edu/](https://link.zhihu.com/?target=https%3A//mimic.mit.edu/)
   来自MIT Lab for Computational Physiology的公共数据集，收集超过60000 ICU的数据，包括病人的人口统计数据、生理体征、实验室测试和[药物治疗](https://www.zhihu.com/search?q=药物治疗&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})等。
2. **[千人基因组计划](https://www.zhihu.com/search?q=千人基因组计划&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})**

链接：[https://aws.amazon.com/cn/1000genomes/](https://link.zhihu.com/?target=https%3A//aws.amazon.com/cn/1000genomes/)

千人基因组计划是一项国际科研合作项目，目前已经建立了最详细的人类基因变异图谱，其中包括SNP、[结构性变异](https://www.zhihu.com/search?q=结构性变异&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})及其单倍体环境。项目的最终阶段采集了世界各地26个种群的2500多人的基因序列，并建立了一整套分阶段的单倍体，其中包括这些个体的超过8000万变异。

## [数据管理工具](https://www.zhihu.com/search?q=数据管理工具&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})

1. **Data Version Control (DVC)**
   官网链接：[https://dvc.org/](https://link.zhihu.com/?target=https%3A//dvc.org/)
   Git链接：[https://github.com/iterative/dvc?ref=thechiefio](https://link.zhihu.com/?target=https%3A//github.com/iterative/dvc%3Fref%3Dthechiefio)
   DVC是以Python语言编写的用于数据科学和机器学习项目的开源工具。它采用类似Git的模型来提供数据集和机器学习模型的管理和版本控制。DVC是一个简单的[命令行](https://www.zhihu.com/search?q=命令行&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})工具，可使机器学习项目共享和可复制。

![img](https://picx.zhimg.com/80/v2-c13738ee80c300cd26fd7bed5576858b_1440w.webp)

1. **Pachyderm**

官网链接：[https://www.pachyderm.com/](https://link.zhihu.com/?target=https%3A//www.pachyderm.com/)

Git链接：[https://github.com/pachyderm/pachyderm?ref=thechiefio](https://link.zhihu.com/?target=https%3A//github.com/pachyderm/pachyderm%3Fref%3Dthechiefio)

与DVC一样，Pachyderm是机器学习和[数据科学](https://www.zhihu.com/search?q=数据科学&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra={"sourceType"%3A"answer"%2C"sourceId"%3A"2928765090"})的版本控制工具。除此之外，它基于Docker和Kubernetes构建，这有助于它在任何云平台上运行和部署机器学习项目。Pachyderm可以确保机器学习模型中的每一个数据都是可版本化和可追溯的。

![img](https://pica.zhimg.com/80/v2-a4b7a505fc98216a045cb222232327a0_1440w.webp)