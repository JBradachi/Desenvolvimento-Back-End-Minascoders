from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permitir requisições de diferentes origens

# Configurações do MySQL
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'rafaella'
app.config['MYSQL_PASSWORD'] = '10062005'  # Senha do MySQL
app.config['MYSQL_DB'] = 'mysqlsite'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

# Configuração para mensagens flash
app.secret_key = 'sua_chave_secreta_aqui'

mysql = MySQL(app)

# Rota para exibir notícias
@app.route('/noticias')
def noticias():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM noticia ORDER BY data_publicacao DESC")
    noticias = cur.fetchall()
    cur.close()
    return render_template('noticias.html', noticias=noticias)

# Rota para adicionar notícias
@app.route('/adicionar_noticia', methods=['GET', 'POST'])
def adicionar_noticia():
    if request.method == 'POST':
        # Obtendo os dados do formulário
        titulo = request.form['titulo']
        resumo = request.form['resumo']
        autor = request.form['autor']
        imagem = request.form['imagem']
        data_publicacao = request.form['data_publicacao']

        # Validando os dados
        if not titulo or not resumo or not autor or not imagem or not data_publicacao:
            flash('Todos os campos são obrigatórios!', 'error')
        else:
            # Inserindo a notícia no banco de dados
            cur = mysql.connection.cursor()
            try:
                cur.execute(
                    "INSERT INTO noticia (titulo, resumo, autor, imagem, data_publicacao) VALUES (%s, %s, %s, %s, %s)",
                    (titulo, resumo, autor, imagem, data_publicacao)
                )
                mysql.connection.commit()
                flash('Notícia adicionada com sucesso!', 'success')
            except Exception as e:
                mysql.connection.rollback()
                flash(f'Erro ao adicionar notícia: {str(e)}', 'error')
            finally:
                cur.close()

        return redirect(url_for('noticias'))

    # Se o método for GET, exibe o formulário
    return render_template('adicionar_noticia.html')

# Rota para exibir participantes
@app.route('/participantes')
def participantes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM participantes")
    participantes = cur.fetchall()
    cur.close()
    return render_template('participantes.html', participantes=participantes)

# Rota para exibir patrocinadores
@app.route('/patrocinadores')
def patrocinadores():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patrocinadores")
    patrocinadores = cur.fetchall()
    cur.close()
    return render_template('patrocinadores.html', patrocinadores=patrocinadores)

if __name__ == '__main__':
    app.run(debug=True)
