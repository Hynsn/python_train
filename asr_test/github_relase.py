import requests

# 设置GitHub仓库的用户名和仓库名
username = 'k2-fsa'
repository = 'sherpa-onnx'


# 参考：https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#list-releases
def get_release():
    # 构建API的URL
    url = f'https://api.github.com/repos/{username}/{repository}/releases?per_page=100'

    # 发送HTTP GET请求
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 解析JSON响应
        release = list(response.json())
        for (i, item) in enumerate(release):
            url = item['tarball_url']
            tag_name = item['tag_name']
            body = item['body']
            print(f'--->{i},{tag_name}')
            if str(url).__contains__('models'):
                assets = list(item.get('assets'))
                print(f'--->{url}')
                for asset in assets:
                    name = asset['name']
                    download_url = asset['browser_download_url']
                    print(f'-->{name}')
                # print(f'--->{url}')
                # print(f'--->{item}')
        # 打印最新Release的下载链接
        # for asset in release['assets']:
        #     print(asset['browser_download_url'])
    else:
        print(f'Failed to retrieve release information: {response.status_code}')


# 参考：https://docs.github.com/en/rest/releases/releases?apiVersion=2022-11-28#get-a-release-by-tag-name
def get_tag(tag: str):
    url = f'https://api.github.com/repos/{username}/{repository}/releases/tags/{tag}'
    response = requests.get(url)
    if response.status_code == 200:
        ret = response.json()
        assets = list(ret.get('assets'))
        print(f'--->{url}')
        for asset in assets:
            name = asset['name']
            download_url = asset['browser_download_url']
            print(f'-->{name},{download_url}')
        # print(ret)


if __name__ == '__main__':
    # get_release()
    get_tag('asr-models')
