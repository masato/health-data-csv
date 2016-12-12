# 「ヘルスケア」データCSVコンバーター

```bash
$ docker run -it --rm \
  -v $PWD:/app \
  -w /app \
  continuumio/anaconda3 \
  python convert.py 書き出す.zip 2016-12-01
```
