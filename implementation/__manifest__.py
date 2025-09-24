{
    'name': 'Odoo implementation',
    'version': '1.0',
    'author': 'Lopes Bongo Olualinet',
    'summary': 'Implementaçao Odoo',
    'description':'Desafio 1.0 Odoo Implementation',
    'depends' : ['base'],
    'report': [

       'report/ir.model.access.csv',

        'views/client_views.xml',
        'views/solution_views.xml',
        'views/meno_principal.xml',
    ]
}
