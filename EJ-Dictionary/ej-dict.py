import requests
from bs4 import BeautifulSoup

# 無限ループ
while(1):
    word = input('>>')
    word.replace(' ','+') #半角スペースを+で置換

    # 単語をURLに指定して検索しHTMLを取得
    res = requests.get('https://ejje.weblio.jp/content/{}'.format(word))

    # HTMLからBeautifulSoupのオブジェクトを作成
    soup = BeautifulSoup(res.text, 'html.parser')

    try:
        # HTMLからclass名を指定して検索
        result = soup.find(class_='content-explanation')
        print(result.get_text())
        
    except:
        print('「{}」に一致する見出し語が見つかりません。'.format(word))

    print('')
