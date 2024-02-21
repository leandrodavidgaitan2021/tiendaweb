"""
CuentaCorriente:
ID_cuenta (clave primaria)
ID_cliente (clave foránea hacia Clientes)
Saldo
"""

from tienda import db

# Modelo para la tabla de Cuenta Corriente
class CuentaCorriente(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cliente_id = db.Column(db.Integer)  
    saldo = db.Column(db.Integer)
    
    def __init__(self, cliente_id, saldo):
        self.clienter_id = cliente_id
        self.saldo = saldo