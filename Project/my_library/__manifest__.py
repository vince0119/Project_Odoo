{
    'name': "my_library",
    'summary': """abc""",
    'description': """abc""",
    'author': "vince.info",
    'website': "https://vince.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}