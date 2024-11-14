from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Armazenamento de produtos na memória
produtos = []

@app.route('/')
def index():
    return render_template('index.html', produtos=produtos)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nome = request.form['nome']
        categoria = request.form['categoria']
        preco = float(request.form['preco'])
        quantidade = int(request.form['quantidade'])
        
        novo_produto = {
            'id': len(produtos) + 1,
            'nome': nome,
            'categoria': categoria,
            'preco': preco,
            'quantidade': quantidade
        }
        produtos.append(novo_produto)
        return redirect(url_for('index'))
    
    return render_template('add_product.html')

@app.route('/edit/<int:produto_id>', methods=['GET', 'POST'])
def edit_product(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if request.method == 'POST':
        produto['nome'] = request.form['nome']
        produto['categoria'] = request.form['categoria']
        produto['preco'] = float(request.form['preco'])
        produto['quantidade'] = int(request.form['quantidade'])
        return redirect(url_for('index'))
    
    return render_template('edit_product.html', produto=produto)

@app.route('/delete/<int:produto_id>')
def delete_product(produto_id):
    global produtos
    produtos = [p for p in produtos if p['id'] != produto_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

