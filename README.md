# 与获取BILIBILI视频信息有关的爬虫+API访问

这个项目提供了一个通过UP主ID获取全部发布视频信息，以及根据视频号(BVID)获取视频信息，如播放量，点赞数，视频字幕等。

## 主要功能：
- 获取UP主发布的所有视频信息
- 获取视频的详细视频信息，视频字幕

### 1. 获取视频的详细信息

```bash
pip install requests bs4
```

直接通过api访问，注意要使用cookies才更容易成功
cookies可以在登陆b站后，在网页通过`F12`-`网络` 监听与bilibili的通信获得
可以在每次调用接口时传入cookies，也可以将cookies写入`bili_api/cookie.txt`

注意: api滥用会导致对应api功能暂时封禁！！
所有访问api获取视频信息的方法在`bili_api`中，详细返回值示例在`bili_api/response_demo`


### 2. 获取UP主所有视频信息
需要用到`selenium`爬取
```bash
pip install selenium bs4
pip install tqdm
```

然后安装`chrome`和对应版本的`chrome driver`，注意第一个点之前的版本号一定要对应

这里提供Ubuntu上安装流程，其余系统自己搜索: 
1. 安装chrome，比如我从里面选择了104.0.5112.102
    - [Slimjet - 旧版本的chrome](https://www.slimjet.com/chrome/google-chrome-old-version.php)
    
    ```bash
    sudo dpkg -i google-chrome-stable_current_amd64.deb  # 安装下载的chrome安装包
    sudo apt-get -f install  # 解决依赖关系
    sudo apt-mark hold google-chrome-stable  # 锁定 Chrome 版本，防止自动更新
    ```
   
2. 安装chrome driver
    ```bash
    wget https://chromedriver.storage.googleapis.com/104.0.5112.79/chromedriver_linux64.zip  # 获取104.0.5112.79版本的chromedriver
    unzip chromedriver_linux64.zip
    ```
