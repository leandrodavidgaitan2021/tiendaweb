from tienda.modelos import articulo, proveedor, categoria, cliente, caja, venta, compra, detalle_compra, detalle_venta
from datetime import datetime


# ********************* Busquedas de ARTICULOS

def buscar_articulos(q):
    return articulo.Articulo.query.filter(
            articulo.Articulo.articulo.contains(q) | 
            articulo.Articulo.codart.contains(q) |
            articulo.Articulo.proveedor.contains(q) |
            articulo.Articulo.tipo.contains(q))

def buscar_id_articulo(id):
    return articulo.Articulo.query.get_or_404(id)


def buscar_cod_articulo(_codart):
    return articulo.Articulo.query.filter_by(codart = _codart).first()

def buscar_tipo_articulo(_tipo):
    return articulo.Articulo.query.filter_by(tipo = _tipo).all()


def buscar_proveedor_articulo(_proveedor):
    return articulo.Articulo.query.filter_by(proveedor = _proveedor).all()

def buscar_todos_articulos():
    return articulo.Articulo.query.all()

def buscar_todos_provee_tipo_articulos(_proveedor, _tipo):
    return articulo.Articulo.query.filter_by(proveedor = _proveedor).filter_by(tipo = _tipo).all()    



# ********************* Busquedas de PROVEEDORES
def buscar_todos_proveedores():
    return proveedor.Proveedor.query.all()

def buscar_q_proveedores(q):
    return proveedor.Proveedor.query.filter(proveedor.Proveedor.razonsocial.contains(q))

def buscar_razon_proveedores(_razonsocial):
    return proveedor.Proveedor.query.filter_by(razonsocial = _razonsocial).first()

def buscar_id_proveedor(id):
    return proveedor.Proveedor.query.get_or_404(id)
     
    



# ********************* Busqueda de CATEGORIAS    
def buscar_todas_categorias():   
    return categoria.Categoria.query.all()

def buscar_q_categorias(q):
    return categoria.Categoria.query.filter(categoria.Categoria.categoria.contains(q))

def buscar_categoria(_categoria):
    return categoria.Categoria.query.filter_by(categoria = _categoria).first()

def buscar_id_categoria(id):
    return categoria.Categoria.query.get_or_404(id)



# ********************* Busquedas de CLIENTES
def buscar_todos_clientes():
    return cliente.Cliente.query.all()

def buscar_q_clientes(q):
    return cliente.Cliente.query.filter(cliente.Cliente.nombre.contains(q))

def buscar_nombre_clientes(_nombre):
    return cliente.Cliente.query.filter_by(nombre = _nombre).first()

def buscar_id_clientes(id):
    return cliente.Cliente.query.get_or_404(id)




# ********************* FECHAS

def fecha_hora_actual():
    return datetime.now().strftime("%Y-%m-%d")

def guarda_fecha(fecha_data):
    return datetime.strptime(fecha_data, "%Y-%m-%d").date()




# ********************* COMPRAS
def buscar_compra(identifica):
    return compra.Compra.query.filter_by(id = identifica).first()


# ********************* DETALLE COMPRAS
def buscar_detalle_compra(compraid_id):
    return detalle_compra.DetalleCompra.query.filter_by(compra_id = compraid_id).all()




# ********************* VENTAS
def buscar_venta(identifica):
    return venta.Venta.query.filter_by(id = identifica).first()



# ********************* DETALLE VENTAS
def buscar_detalle_venta(ventaid_id):
    return detalle_venta.DetalleVenta.query.filter_by(venta_id = ventaid_id).all()




# ********************* CAJAS

def buscar_operacion(identificador):
    return caja.Caja.query.get_or_404(identificador)
     

# def get_proveedor(identificador):
#     proveedor_buscado = proveedor.Proveedor.query.filter_by(id = identificador).first()
#     return proveedor_buscado.razonsocial

# def get_cliente(identificador):
#     cliente_buscado = cliente.Cliente.query.filter_by(id = identificador).first()
#     return cliente_buscado.nombre





def get_compra(identifica):
    detalles = []
    
    compraid = buscar_compra(identifica)

    proveedor_buscado = buscar_id_proveedor(compraid.proveedor_id)
    
    detalle_compra_buscada = buscar_detalle_compra(compraid.id)

    for detalle_art in detalle_compra_buscada:
        
        articulo_buscado = buscar_id_articulo(detalle_art.articulo_id)
        
        if articulo_buscado:
            detalle ={
                'articulo' : articulo_buscado.articulo,
                'cantidad' : detalle_art.cantidad,
                'precio_unitario' : detalle_art.precio_unitario
            }
            detalles.append(detalle)
            
    return proveedor_buscado, detalles




def get_venta(identifica):

    detalles = []

    ventaid = buscar_venta(identifica)

    cliente_buscado = buscar_id_clientes(ventaid.cliente_id)    
    
    detalle_venta_buscada = buscar_detalle_venta(ventaid.id)
    
    for detalle_art in detalle_venta_buscada:

        articulo_buscado = buscar_id_articulo(detalle_art.articulo_id)

        if articulo_buscado:
            detalle = {
                'articulo' : articulo_buscado.articulo,
                'cantidad' : detalle_art.cantidad,
                'precio_unitario' : detalle_art.precio_unitario
            }
            detalles.append(detalle)

    return cliente_buscado, detalles

