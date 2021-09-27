# モザイクアートを作ろう

Thanks: https://zenn.dev/eetann/books/2020-09-25-make-mosaic-art-python

## ファイルの説明

- get-block-img.py
	- Chapter 03 で画像のURLを取得してくるコード

- main.py
	- モザイクアートを生成する処理を行うファイル


## 実行方法

clone & cd:
```shell
git clone https://github.com/zztkm/mosaic-art-practice.git
cd mosaic-art-practice
```

依存ライブラリのインストール:
```shell
python -m venv venv
# activate your venv
(venv) pip install -r requirements.txt
```

モザイクアート化する画像を`main.py`があるフォルダに配置 or 画像のURLを準備.

画像の準備ができたら以下のどちらかのように実行

フォルダに配置した場合:
```shell
(venv) python main.py test.jpg
```

URLの場合:
```
(venv) python main.py https://images.metmuseum.org/CRDImages/es/web-large/DT7115.jpg
```