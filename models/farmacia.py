# Modelo que permite la gestión de una farmacia


from odoo import models, fields

class Producto(models.Model):
	_name = 'farmacia.producto'
	_description = 'Modelo que permite la gestión de los productos de una farmacia.'
	codigo = fields.Char('Código', required=True)
	nombre_producto = fields.Char('Producto', required=True)
	tipo_producto = fields.Selection([('1', 'Mediacamento'), ('2', 'Higiene'), ('3','Cosmética'), ('4','Nutrición'), ('5','Suplementos')])
	caducidad = fields.Date('Fecha de caducidad', required=True)
	marca = fields.Char('Marca', required=True)
	cantidad = fields.Integer('Cantidad', required=True)
	pa = fields.Char('Principio activo')
	presentacion = fields.Char('Presentación farmacológica')
	dosis = fields.Integer('Dosis')
	precio = fields.Float('Precio', required=True)
	receta = fields.Selection([('1', 'Sí'), ('2', 'No')])
	foto = fields.Binary(string='Imagen')
	herencia_ids = fields.Many2many('farmacia.receta', string='Receta')



class Receta(models.Model):
	_name = 'farmacia.receta'
	_description = 'Modelo para la gestión de las recetas de una farmacia.'
	codigo_receta = fields.Char('Código', required=True)
	nombre_paciente = fields.Char('Paciente', required=True)
	cip = fields.Char('CIP', required=True)
	fecha_nacimiento = fields.Date('Fecha de nacimiento del paciente', required=True)
	centro = fields.Char('Centro médico', required=True)
	direccion_centro = fields.Char('Dirección centro médico')
	telf = fields.Char('Teléfono Centro')
	poblacion = fields.Char('Población Centro')
	provincia = fields.Integer('Provincia')
	nombre_medico = fields.Char('Médico', required=True)
	nombre_mediacamento = fields.Char('Nombre medicamento', required=True)
	presentacion = fields.Char('Presentación farmacológica')
	principio_activo = fields.Char('Principio Activo')
	posologia = fields.Char('Posología')
	fecha_caducidad = fields.Date('Fecha de Caducidad', required=True)
	fecha_expedicion = fields.Date('Fecha de expedición', required=True)
	tsi = fields.Char('TSI', required=True)
	formato = fields.Selection([('1','Papel'),('2','Electrónica')])
	emisor = fields.Selection([('1','Sanidad Pública'), ('2','MUJEJU'), ('3','MUFACE'), ('4','ISFAS')])
	tipo_medicamento = fields.Selection([('1', 'Mediacamento'), ('2', 'Psicotropo'), ('3', 'Estupefaciente')], required=True)