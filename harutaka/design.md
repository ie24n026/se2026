# 設計

## 画面(入出力の例)
python movie.py <サブコマンド> [引数]

### サブコマンド：
- add <title> [ジャンル] [評価]   映画を追加
- edit <title>　　　　　　        映画を編集  
- rm <title>                     映画を削除
- list                           映画一覧
- search <title>                 映画名で検索
- stats　　　　　　               統計を表示

### 実行サンプル：
```
$python movie.py add "君の名は" アニメ 5
追加した（合計1件）
$python movie.py list
1. 君の名は / アニメ / 評価:5
```

## データ
### movies.csv
1つの映画に対して、タイトル・ジャンル・評価・感想を保存する。
```
title, genre, rating, comment
君の名は, アニメ, 5, 感動した
インセプション, SF, 4, 難しいけど面白い
```

## 処理の流れ
### add
1. 引数からtitle、genre、ratingを取る
2. commentが無ければ対話で聞く
3. movies.csvを読む
4. 同じtitleがすでにあれば、エラーで止める（変更したい場合はeditを使う）
5. 追加して書き戻す

### edit
1. 引数からtitleを取る
2. movies.csvを読む
3. 同じtitleの映画を探す
4. 新しいジャンル、評価、感想を入力する
5. 変更して書き戻す

### rm
1. 引数からtitleを取る
2. movies.csvを読む
3. 同じtitleの映画を探す
4. 見つかった映画を削除する
5. 書き戻す

### list
1. movies.csvを読む
2. 登録されている映画を一覧で表示する

### search
1. 引数からtitleを取る
2. movies.csvを読む
3. titleを含む映画を探す
4. 見つかった映画を表示する

### stats
1. movies.csvを読む
2. 登録件数を数える
3. 評価の平均を計算する
4. 統計を表示する

## 構成
- movie.py     実装本体
- movies.csv   映画データ

文字コード：UTF-8固定
ライブラリ：Python標準ライブラリのみ
