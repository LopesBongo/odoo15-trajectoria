{
    'name': 'Medical Appointments',
    'version': '1.0',
    'author': 'Lopes Bongo Olualinet',
    'summary': 'Implementaçao Odoo',
    'description': 'Desafio 1.2 Gestão de Consultas Médicas',
    'depends': ['base'],
    'report': [

        'report/ir.model.access.csv',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/appointment_views.xml',
        'views/meno_principal.xml',
    ]
}
