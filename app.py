import os
from flask import Flask, render_template, request, redirect
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "fallback-dev")

WHATSAPP_NUMBER = os.getenv("WHATSAPP_NUMBER")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/avaliacao', methods=['GET', 'POST'])
def avaliacao():
    if request.method == 'POST':

        if not WHATSAPP_NUMBER:
            return "Número do WhatsApp não configurado", 500

        nome = request.form.get('nome')
        idade = request.form.get('idade')
        altura = request.form.get('altura')
        peso = request.form.get('peso')
        objetivo = request.form.get('objetivo')
        atividade = request.form.get('atividade')
        restricoes = request.form.get('restricoes')

        mensagem = f"""
Olá, Renato!

Acabei de preencher a pré-avaliação no seu site.
Seguem meus dados:

Nome: {nome}
Objetivo: {objetivo}
Nível de atividade: {atividade}

Altura: {altura} cm
Peso: {peso} kg
Idade: {idade}

Restrições:
{restricoes if restricoes else "Nenhuma informada"}

Gostaria de conversar sobre a consultoria personalizada.
"""

        texto = quote_plus(mensagem)
        whatsapp_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={texto}"

        return redirect(whatsapp_url)

    return render_template('assessment.html')

if __name__ == "__main__":
    app.run(debug=True)


    