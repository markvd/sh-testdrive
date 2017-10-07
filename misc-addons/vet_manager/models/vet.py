from odoo import api, fields, models, _


class Vet(models.Model):
    _name = "vet_manager.vet"
    _inherit = "res.partner"

    name = fields.Char(string="Vet name", required=True, translate=True, )
