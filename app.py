from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'e153c8a11321db062e9e6f4706574dcd982af35a78e8a24d05c83d22eef4c9b2'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/avaliacao', methods=['GET', 'POST'])
def assessment():
    if request.method == 'POST':
        # Coleta de dados do formulário
        dados_cliente = {
            "nome": request.form.get('nome'),
            "objetivo": request.form.get('objetivo'),
            "peso": request.form.get('peso'),
            # Aqui você poderia salvar em um banco de dados ou enviar por e-mail
        }
        
        # Simulação de processamento de dados
        print(f"Nova Consultoria Recebida: {dados_cliente}")
        
        flash('Obrigado, Renato entrará em contato em breve!', 'success')
        return redirect(url_for('index'))
    
    return render_template('assessment.html')

if __name__ == '__main__':
    app.run(debug=True)