{
    'name': "Book Category",
    'summary': """Module to manage book categorization""",
    'description': """This module enables the user to manage books categorization, specifically two categories:
- Programming books
- IT books
IT books are the parent category of programming books.""",
    'author': "minhng.info",
    'website': "https://minhng.info",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/bookcategory_view.xml',
        # 'views/my_library_form.xml',
        # 'views/library_class_form.xml'
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}