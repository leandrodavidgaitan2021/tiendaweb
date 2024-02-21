from flask import Blueprint, render_template, request, url_for, redirect, flash, g, jsonify, json

# Importamos funcion para que que las vistas sea requerido logearse
from tienda.routers.auth import login_required, login_admin
from tienda.routers.busquedas import *


from tienda.modelos import caja
from tienda import db


bp = Blueprint('cajas', __name__, url_prefix='/cajas')



# Lista los productos antes de logearse
@bp.route('/lista', methods = ["GET", "POST"])
@login_admin
@login_required
def lista():
    # fecha actual
    fecha_actual = fecha_hora_actual()
    # se toma id usuario
    id = g.user.id
   

    # se guardan todas las cajas por id usuario = creado_por
    _cajas = caja.Caja.query.order_by(caja.Caja.id.desc()).filter(caja.Caja.creado_por.contains(id)).all()

    # se inicializan las variales totales
    total_compra_efectivo = 0
    total_compra_billetera = 0
    total_venta_efectivo = 0
    total_venta_billetera = 0
    total_venta_cuenta_corriente = 0
    total_venta_cobrado_a_efectivo = 0
    total_venta_cobrado_a_billetera = 0
    total_transferencia_a_efectivo = 0
    total_transferencia_a_billetera = 0
     
    # se busca los tipo de ventas y se guarda por tipo de caja el monto   
    for _caja in _cajas:
        if _caja.tipo == "V":
            if _caja.caja == "E":
                total_venta_efectivo += _caja.monto
            if _caja.caja == "B":
                total_venta_billetera += _caja.monto
            if _caja.caja == "C":
                total_venta_cuenta_corriente += _caja.monto    
        elif _caja.tipo == "C":
            if _caja.caja == "E":
                total_compra_efectivo += _caja.monto
            if _caja.caja == "B":
                total_compra_billetera += _caja.monto
        elif _caja.tipo == "T":
            if _caja.caja == "E":
                total_transferencia_a_efectivo += _caja.monto
            if _caja.caja == "B":
                total_transferencia_a_billetera += _caja.monto
        elif _caja.tipo == "P":
            if _caja.caja == "E":
                total_venta_cobrado_a_efectivo += _caja.monto
            if _caja.caja == "B":
                total_venta_cobrado_a_billetera += _caja.monto


           
                        
    # se envia todo a la pagina
    return render_template('caja/lista.html', 
                           cajas = _cajas, 
                           t_e_compra = total_compra_efectivo, 
                           t_b_compra = total_compra_billetera,
                           t_e_venta = total_venta_efectivo, 
                           t_b_venta = total_venta_billetera,
                           t_c_venta = total_venta_cuenta_corriente,
                           t_p_e_venta = total_venta_cobrado_a_efectivo,
                           t_p_b_venta = total_venta_cobrado_a_billetera,
                           t_transf_a_efectivo = total_transferencia_a_efectivo,
                           t_transf_a_billetera = total_transferencia_a_billetera, 
                           fecha = fecha_actual
                           )



@bp.route('/transferir', methods = ["GET", "POST"])
@login_admin
@login_required
def transferir():
    # Obtiene los datos enviados desde el cliente
    data = request.get_json()  
    _fecha = data['fecha'] # Datos del lado del cliente, fecha seleccionado
    _fecha = guarda_fecha(_fecha)
    tipo_moviento = data['opcion']  # Datos del lado del cliente, tipo movimiento
    monto = data['monto'] # Datos del lado del cliente, monto

    tipo_ = "T"
    id_tipo_ = 0
    monto_ = int(monto)
    creado_por_ = g.user.id
    
    if tipo_moviento == "A EFECTIVO":
        caja_ = "E"
        caja_ = caja.Caja(_fecha, tipo_, id_tipo_, caja_, monto_, creado_por_)
        db.session.add(caja_)
        db.session.commit()
    elif tipo_moviento == "A BILLETERA":
        caja_ = "B"
        caja_ = caja.Caja(_fecha, tipo_, id_tipo_, caja_, monto_, creado_por_)
        db.session.add(caja_)
        db.session.commit()
    
    return redirect(url_for('cajas.lista'))





@bp.route('/ver_operacion/<int:id>', methods = ["GET"])
@login_required
@login_admin
def ver_operacion(id):
    
    operacion = buscar_operacion(id)
    
    if operacion.tipo == "C":
        aquien, detalles = get_compra(operacion.id_tipo)
    if operacion.tipo == "V":
        aquien, detalles = get_venta(operacion.id_tipo)
        
    if operacion.tipo == "T":
        if operacion.caja == "E":
            detalles = f"El dia {operacion.fecha}, se transfirio de Billetera a Efectivo, ${operacion.monto}"
        if operacion.caja == "B":
            detalles = f"El dia {operacion.fecha}, se transfirio de Efectivo a Billetera, ${operacion.monto}"
        aquien = 'Silvana'
    return render_template('caja/ver_operacion.html', operacion = operacion, detalles = detalles, aquien = aquien)

