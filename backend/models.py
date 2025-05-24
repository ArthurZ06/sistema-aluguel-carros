from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(100))
    placa = db.Column(db.String(20))
    dataTroca = db.Column(db.String(20))
    km = db.Column(db.Integer)
    proximaTroca = db.Column(db.Integer)
    dataAtual = db.Column(db.String(20))
    kmAtual = db.Column(db.Integer)
    observacao = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "modelo": self.modelo,
            "placa": self.placa,
            "dataTroca": self.dataTroca,
            "km": self.km,
            "proximaTroca": self.proximaTroca,
            "dataAtual": self.dataAtual,
            "kmAtual": self.kmAtual,
            "observacao": self.observacao
        }
