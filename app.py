import pandas as pd
import feedgenerator
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    df = pd.read_csv(file, sep=';', header=None, names=['codigo', 'produto', 'preco', 'unidade'])

    feed = feedgenerator.Rss201rev2Feed(
        title='Lista de Preços',
        link='https://seusite.com/precos',
        description='Lista de preços de produtos'
    )

    for index, row in df.iterrows():
        item = feedgenerator.RssItem(
            title=row['produto'],
            link=f'https://seusite.com/produto/{row["codigo"]}',  # Link dinâmico baseado no código
            description=f'{row["preco"]} {row["unidade"]}'
        )
        feed.add_item(item)

    # Salva o feed em um arquivo (ajuste o caminho conforme necessário)
    feed.write('static/rss.xml')

    # Retorna o link para o feed
    return jsonify({'link': 'https://seusite.com/static/rss.xml'})

if __name__ == '__main__':
    app.run(debug=True)