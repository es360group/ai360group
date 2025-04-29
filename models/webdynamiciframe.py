from odoo import models, fields

class AIgroup360Iframe(models.Model):
    _name = "aigroup360.iframe"
    _description = "Web Dynamic Iframe"

    name = fields.Char('Name', required=True, default='AI360Group', readonly=True)