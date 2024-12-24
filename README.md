### 環境構築手順

#### 仮想環境の作成

```bash
sudo apt install python3-venv
python3 -m venv venv
```

#### 仮想環境を起動

```bash
source venv/bin/activate
```

#### pip を最新化

```bash
pip install --upgrade pip
```

#### Streamlit のインストール

```bash
pip install streamlit
```

#### バージョン確認

```bash
streamlit --version
```

#### サンプルアプリを起動

```bash
streamlit hello
```

#### ファイル名を指定して起動

```bash
streamlit run app.py
```

#### 仮想環境を終了

```bash
deactivate
```

### API リファレンス

[API Reference - Streamlit Docs](https://docs.streamlit.io/develop/api-reference)

### 疑問点

- スタイルを当てる場合は組み込みコンポーネントの使用が推奨されているのか
- 実際の現場では、スタイルにこだわるか
- アニメーションはどうする
- pandas, matplotlib の勉強はどうする
- ディレクトリ構成のベストプラクティス
