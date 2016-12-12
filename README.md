# ヘルスケアデータCSVコンバーター

## 使い方

リポジトリをcloneします。

```bash
$ git clone https://github.com/masato/health-data-csv.git
$ cd health-data-csv
```

iPhoneの「ヘルスケア」アプリからヘルスケアデータを書き出します。
「書き出す.zip」ファイルをcloneしたディレクトリにコピーします。

ZipファイルからXMLを取り出し歩数データをCSVにコンバートします。
以下の例では2016-12-01からのデータを対象にします。

```bash
$ docker run -it --rm \
  -v $PWD:/app \
  -w /app \
  continuumio/anaconda3 \
  python convert.py -f 書き出す.zip -s 2016-12-01
```
