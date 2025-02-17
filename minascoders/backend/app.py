from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import mysql.connector
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)


UPLOAD_FOLDER = 'images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def testeHome():
    return render_template("index.html")

@app.route('/noticias')
def noticias():
    cur = mydb.cursor()
    cur.execute("SELECT * FROM noticia ORDER BY data_publicacao DESC")
    noticias = cur.fetchall()
    cur.close()

    # Faz o tratamento dos dados
    noticiasTratadas = list()
    for noticia in noticias:
        noticiasTratadas.append(
            {
            'id': noticia[0],
            'titulo': noticia[1],
            'data_publicacao': noticia[2],
            'resumo': noticia[3],
            'autor': noticia[4],
            'imagem': noticia[5]
            }
        )

    return render_template('noticias.html', noticias=noticiasTratadas)

@app.route('/adicionarNoticia', methods=['GET', 'POST'])
def adicionar_noticia():
    if request.method == 'POST':
        # Obtendo os dados do formulário
        titulo = request.form['titulo']
        resumo = request.form['resumo']
        autor = request.form['autor']
        #imagem = request.form['imagem']
        data_publicacao = request.form['data']

        # Validando os dados
        if not titulo or not resumo or not autor or not data_publicacao:
            flash('Todos os campos são obrigatórios!', 'error')
        else:
            # Inserindo a notícia no banco de dados
            
            try:
                if 'imagem' not in request.files:
                    return 'Nenhum arquivo enviado', 400

                file = request.files['imagem']

                if file.filename == '':
                    return 'Nenhum arquivo selecionado', 400

                # Crie a pasta 'uploads' se não existir
                if not os.path.exists(UPLOAD_FOLDER):
                    os.makedirs(UPLOAD_FOLDER)
                
                filename = os.path.join(UPLOAD_FOLDER, secure_filename(file.filename))

                file.save(filename)

                imagem = filename

                cur = mydb.cursor()
                cur.execute(
                    "INSERT INTO noticia (titulo, resumo, autor, imagem, data_publicacao) VALUES (%s, %s, %s, %s, %s)",
                    (titulo, resumo, autor, imagem, data_publicacao)
                )
                mydb.commit()

                flash('Notícia adicionada com sucesso!', 'success')
            except Exception as e:
                mydb.rollback()
                flash(f'Erro ao adicionar notícia: {str(e)}', 'error')
            
            cur.close()

        return redirect(url_for('noticias'))

    # Se o método for GET, exibe o formulário
    return render_template('adicionarNoticia.html')

@app.route('/noticias/<filename>')
def servidorDeImagem():
    pass

if __name__ == "__main__":

    # Conecta com o banco
    app_host='db'
    app_user='root'
    app_password='root'
    app_database='mysqlsite'
    

    # Como o container do banco demora para iniciar
    # o algorítmo fica tentando conectar até ele
    # liberar as conexões e de fato conectar
    # a solução dessa gambiarra seria usar Kubernetes talvez
    try:
        mydb = mysql.connector.connect(
            host=app_host,
            user=app_user,
            password=app_password,
            database=app_database,
        )
    except Exception as error:
        print("Banco de dados não conectado", error)
        exit()

    print("Banco conectado")

    app.secret_key = 'super secret key'

    app.run(debug=True, port=5000, host='0.0.0.0')