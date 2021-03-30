from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel
from random import choice
@app.route('/productos')
def productos():
    productosModel =ProductosModel()

    productos = productosModel.traerTodos()
   
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods =['GET', 'POST'])
def crear_producto():
   #esta funcion me sirve para mostrar el formulario de creacion
   #y tambien me sirve para crear un nuevo producto
   #estos pasos se identifican con los metodos 
    if request.method == 'GET':
       #mostramos el formulario de cracion
        return render_template('productos/crear.html')

    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precio_compra = request.form.get('precio_compra')
    precio_venta = request.form.get('precio_venta')
    estado = request.form.get('estado')
    
    if estado == '1':
        estado = 'Activo'
    else:
        estado = 'Inactivo'
      
    productosModel = ProductosModel()

    productosModel.crear(nombre,descripcion,precio_compra,precio_venta,estado)
    

    #aca es la cracion del producto
    return redirect(url_for('productos'))
    # AQUI EMPIEZA EL DESARROLLO DE ACORTAR LINKS
@app.route('/productos/enlace', methods =['GET', 'POST'])
def traer_link():
   
    if request.method == 'GET':
      
        return render_template('/productos/enlace.html')
    else:

        nombre = request.form.get('link')
        longitud = 4
        valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        p = ""
        p = p.join([choice(valores) for i in range(longitud)])

        productosModel = ProductosModel()
        productosModel.insertar_link(nombre,p)
        
        return("El lnk fue Guardado en BD")
        