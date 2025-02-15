from odoo import models,fields,api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    address = fields.Char(string="Address")
    longitude = fields.Char(string="Longitude")
    latitude = fields.Char(string="Latitude")
    ne_latitude = fields.Char(string="North-East Latitude")
    ne_longitude = fields.Char(string="North-East Longitude")
    sw_latitude = fields.Char(string="South-East Latitude")
    sw_longitude = fields.Char(string="South-East Longitude")








































