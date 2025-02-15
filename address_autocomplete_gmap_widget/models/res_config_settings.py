from odoo import models,fields,api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    google_map_api_key = fields.Char(string="Google Map API Key",config_parameter="address_autocomplete_gmap_widget.google_map_api_key")
