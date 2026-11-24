# This file is part of Equivalent Name module.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from trytond.model import ModelView, ModelSQL, fields


class EquivName(ModelSQL, ModelView):
    "Equivalent Name"
    __name__ = "equiv_name.equiv"

    origin = fields.Reference('Origin', selection='get_origin', required=True)
    equivalent = fields.Char('Equivalent', size=200, required=True)

    @classmethod
    def _get_origins(cls):
        origins = ['party.party', 'product.product', 'product.uom']
        return origins

    @classmethod
    def get_origin(cls):
        pool = Pool()
        Model = pool.get('ir.model')
        mdls = cls._get_origins()
        models = Model.search([
                ('name', 'in', mdls),
                ])
        return [('', '')] + [(m.name, m.string) for m in models]