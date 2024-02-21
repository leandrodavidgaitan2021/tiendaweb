"""
Transacciones:
ID_transacción (clave primaria)
ID_cliente (clave foránea hacia Clientes)
Fecha
Tipo (compra, pago, etc.)
Monto
"""

from tienda import db

# Modelo para la tabla de transacciones
class Transaccion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    cliente_id = db.Column(db.Integer)  
    fecha = db.Column(db.Date)
    tipo = db.Column(db.String(20))
    monto = db.Column(db.Integer)
    
    def __init__(self, cliente_id, fecha, tipo, monto):
        self.clienter_id = cliente_id
        self.fecha = fecha
        self.tipo = tipo
        self.monto = monto