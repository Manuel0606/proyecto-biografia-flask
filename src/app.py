from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/felipe')
def felipe():
    biografia = """
    Nací el 28 de Octubre del 2001, pasé mi niñez y parte de mi adolescencia en Bogotá, luego vine a vivir a Chiquinquirá a terminar mis estudios de la secundaria, allí fue donde aprendí a jugar basketball.
    Mis pasatiempos son el basketball, la computación, la música y el emprendimiento.
    En mis metas se encuentra el lograr aportar mis conocimientos y habilidades en beneficio de la sociedad.
    """
    foto_url="images/foto_andres.jpg"
    data = {
        'nombre':'Andrés Felipe Carranza Ruiz',
        'biografia':biografia,
        'foto_url':foto_url
    }
    return render_template('felipe.html', data=data)

@app.route('/manuel')
def manuel():
    biografia = """
    """
    foto_url="images/foto_manuel.jpg"
    data = {
        'nombre':'Manuel Alejandro Comezaña Quintero',
        'biografia':biografia,
        'foto_url':foto_url
    }
    return render_template('manuel.html', data=data)
  
if __name__ == '__main__':
  app.run(debug=True, port=6001)
