from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from models import db, Veiculo

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/veiculos', methods=['GET'])
def listar_veiculos():
    veiculos = Veiculo.query.all()
    return jsonify([v.to_dict() for v in veiculos])

@app.route('/veiculo', methods=['POST'])
def adicionar_veiculo():
    data = request.get_json()
    veiculo = Veiculo(**data)
    db.session.add(veiculo)
    db.session.commit()
    return jsonify(veiculo.to_dict()), 201

@app.route('/veiculo/<int:id>', methods=['PUT'])
def atualizar_km(id):
    data = request.get_json()
    veiculo = Veiculo.query.get_or_404(id)
    veiculo.kmAtual = data['kmAtual']
    veiculo.proximaTroca = veiculo.kmAtual + 60000  # Exemplo: troca a cada 60 mil km
    veiculo.dataAtual = data['dataAtual']
    db.session.commit()
    return jsonify(veiculo.to_dict())

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
