# Cosmos Boys 公式サイト

公開URL: https://cosmosboys.github.io/
確認用アーティファクト: https://claude.ai/artifact/Gm2ht9973B5X7N7PYxhGjA

## 構成
- src/page.html: サイト本体。アーティファクトとして公開しているものと同じファイル
- img/: ジャケット、ロゴ、猫、ogp.jpg(シェア用カード 1200x630)
- index.html: build.py が src/page.html から作る。直接編集しない
- .nojekyll: GitHub Pagesの加工を止める

## 更新の流れ
1. src/page.html を編集する
2. アーティファクトを更新する(Artifact publish、url に上の確認用アーティファクト、file_path に src/page.html)
3. エムがOKを出したら python3 build.py を実行して main に push する
4. 1分ほどで公開URLに反映される

## 決まりごと
- コミットの作者は cosmosboys <344325736+cosmosboys@users.noreply.github.com>。個人のメールアドレスを出さない
- このリポジトリは公開。航行記録の中身 未発表曲 リリース前の歌詞などは置かない
- 英語表記は Cosmos Boys(ロゴやデザイン上の大文字表記は別)
- ファンサイトにライブ情報は出さない。曲ごとの物語はABOUTの厳選5本のみ

## アクセス解析
- Googleアナリティクス 測定ID G-R9GHZS27J1 プロパティ名 Cosmos Boys Official
- タグは src/page.html の head にあり、cosmosboys.github.io 上でだけ読み込む
- 画面を切り替えるたびに page_view を送る。ハッシュは /music /r-signal のようなパスに置き換えて記録
- 数字はWindsor.aiの googleanalytics4 コネクタから取れる(アカウントID 559460320)
- サムネイル: 一覧や小さい表示は img/t/ の600px版を使う(TH)。大きい表示は img/ の1200px版(IMG)
