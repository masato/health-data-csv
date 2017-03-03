# ヘルスケアデータCSVコンバーター

## 使い方

リポジトリをcloneします。

```bash
$ git clone https://github.com/masato/health-data-csv.git
$ cd health-data-csv
```

iPhoneの「ヘルスケア」アプリからヘルスケアデータを書き出します。
「書き出した.zip」ファイルをcloneしたディレクトリにコピーします。

ZipファイルからXMLを取り出し歩数データをCSVにコンバートします。
以下の例では2016-12-01からのデータを対象にします。

```bash
$ docker run -it --rm -v $PWD:/app -w /app continuumio/anaconda3 python convert.py -f 書き出した.zip -s 2016-12-01
```

カレントディレクトリに「steps_xxx.csv」のような歩数を日別に集計したCSVファイルが作成されます。

```bash
$ cat steps_20161212013800.csv
2016-12-01,2016-12-02,2016-12-03,2016-12-04,2016-12-05,2016-12-06,2016-12-07,2016-12-08,2016-12-09,2016-12-10,2016-12-11
7217,8815,2260,1828,3711,6980,7839,5079,7197,7112,2958
```
