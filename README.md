## プレビュー
### main
![main](https://github.com/user-attachments/assets/f489212d-8cda-4b82-8ff7-175a26169a87)

### cols
![cols](https://github.com/user-attachments/assets/87bbd54e-4acb-47b5-899b-597709ba29b8)

### form
![form](https://github.com/user-attachments/assets/8cbe571c-60d2-49cf-a1b5-0b126b61a8e3)

![form_input](https://github.com/user-attachments/assets/76045fe7-2f4e-41c5-8a25-19ba1f945683)

### data graph
![data_graph](https://github.com/user-attachments/assets/ea535dba-1a39-4deb-93a1-813c55dc3038)

### rust code
![rust_code](https://github.com/user-attachments/assets/ca692ca5-cdf1-4372-9336-5afdcc14f389)


## 環境構築手順

### 仮想環境の作成

```bash
sudo apt install python3-venv
python3 -m venv venv
```

### 仮想環境を起動

```bash
source venv/bin/activate
```

### pip を最新化

```bash
pip install --upgrade pip
```

### Streamlit のインストール

```bash
pip install streamlit
```

### バージョン確認

```bash
streamlit --version
```

### サンプルアプリを起動

```bash
streamlit hello
```

### ファイル名を指定して起動

```bash
streamlit run app.py
```

### 仮想環境を終了

```bash
deactivate
```

## API リファレンス

[API Reference - Streamlit Docs](https://docs.streamlit.io/develop/api-reference)

## 疑問点

- スタイルを当てる場合は組み込みコンポーネントの使用が推奨されているのか
- 実際の現場では、スタイルにこだわるか
- アニメーションはどうする
- pandas, matplotlib の勉強はどうする
- ディレクトリ構成のベストプラクティス
