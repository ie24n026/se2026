# 設計

## 画面(入出力の例)
python egjz.py <サブコマンド> [引数]

## データ
### data.csv
1つの英単語に対して、日本語の意味を / 区切りで複数保存できる。
```
english, japanese
apple,リンゴ/りんご/林檎
bear,熊/くま
cat,猫/ネコ
```
### history.csv
クイズの結果を残す。
```
date, score, total
2025-05-13,4,10
```
### 取り込み用ファイル
.csvも.txt も同じ扱い。カンマ区切り。

データ例：
```
apple,りんご
bear,熊
```
ヘッダ行（"english,japanese"）があれば自動でスキップする。

## 処理の流れ
## 構成
