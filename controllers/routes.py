from flask import render_template


def init_app(app):
    # Definindo a rota principal da aplicação '/'
    @app.route('/')
    def home():  # Função que será executada ao acessar a rota
        return render_template('index.html')

    @app.route('/fotos')
    def games():
        title = 'A Santa'
        description = 'Nessa fotografia eu quis retratar a importância simbolica dessa figura religiosa da igreja.'
        url = ''
        date_upload = '03/05/2025'
        return render_template('fotos.html', title=title, description=description, url=url, date_upload=date_upload)
