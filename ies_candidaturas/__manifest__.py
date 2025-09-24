{
    'name': "IES Candidaturas",
    'version': '1.0',
    'summary': "Gestão de candidaturas para Instituições de Ensino Superior",
    'author': "Lopes Cavila",
    'depends': ['base'],
    'report': [
        'report/ir.model.access.csv',
        'views/instituicao_views.xml',
        'views/faculdade_views.xml',
        'views/Curso_views.xml',
        'views/candidatura_views.xml', ],
    'installable': True,
    'application': True,
}
