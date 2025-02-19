from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
import mysql.connector
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

# Configurações
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

    # Requisita um cursor e faz a consulta
    cur = mydb.cursor()
    cur.execute("""SELECT * FROM noticia 
                ORDER BY data_publicacao DESC""")
    
    noticias = cur.fetchall() # Função que tras as info do cursor para uma var
    cur.close() # Importantíssimo fechar o cursor

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
    
    # Passa dados tratados para o html/jinja
    return render_template('noticias.html', noticias=noticiasTratadas)

@app.route('/dashboard/noticia/inserir', methods=['GET', 'POST'])
def adicionarNoticia():
    if request.method == 'POST':

        # Obtendo os dados do formulário
        titulo = request.form['titulo']
        resumo = request.form['resumo']
        autor = request.form['autor']
        data_publicacao = request.form['data']

        try:
            
            filename = salvaImagem('imagem')

            cur = mydb.cursor()
            cur.execute(
                """INSERT INTO noticia 
                (titulo, resumo, autor, imagem, data_publicacao) 
                VALUES (%s, %s, %s, %s, %s)""",
                (titulo, resumo, autor, filename, data_publicacao)
            )

            # Faz commit da consulta de inserção sql
            mydb.commit()

            flash('Notícia adicionada com sucesso!', 'success')

        except Exception as e:
            mydb.rollback()
            flash(f'Erro ao adicionar notícia: {str(e)}', 'error')
        
        cur.close()

        return redirect(url_for('noticias'))

    # Se o método for GET, exibe o formulário
    return render_template('adicionarNoticia.html')

def salvaImagem(idImagem):
    """idImagem é o mesmo id que voce coloca no input
    do html"""

    if idImagem not in request.files:
        return 'Nenhum arquivo enviado', 400

    file = request.files[idImagem]

    # Crie a pasta 'uploads' se não existir
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    filename = os.path.join("", app.config['UPLOAD_FOLDER'], 
                            secure_filename(file.filename))
    
    # Salva a imagem na pasta dedicada
    file.save(filename)

    return filename

@app.route('/images/<filename>')
def servidorDeImagem(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/dashboard', methods=['GET'])
def Dashboard():
       
    return render_template("dashboard.html")

@app.route('/dashboard/noticia', methods=['GET','POST'])
def DashboardNoticia():
        
    return render_template("dashboardNoticia.html")

@app.route('/dashboard/noticia/remover', methods=['GET','POST'])
def removerNoticia():

    cur = mydb.cursor()

    if request.method == 'POST':
        titulo = request.form.get('titulo')

    # Deleta a notícia a partir do título e faz commit ao banco
        if titulo:
            cur.execute("DELETE FROM noticia WHERE titulo = %s", (titulo,))
            mydb.commit()  

    # Atualiza a listagem de notícias pós-remoção
    cur.execute("SELECT * FROM noticia ORDER BY data_publicacao DESC")
    noticias = cur.fetchall()
    cur.close()

    noticiasTratadas = list()
    
    for noticia in noticias:
        noticiasTratadas.append(
            {
            'titulo': noticia[1],
            }
        )
   
    return render_template('removerNoticia.html', noticias=noticiasTratadas)


if __name__ == "__main__": 

    # Conectando com o banco
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

    #TODO: criar arquivo .env e colocar todas as variáveis
    app.secret_key = 'super secret key'

    app.run(debug=True, port=5000, host='0.0.0.0')