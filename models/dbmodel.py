from datetime import datetime

categories = ['noun', 'verb', 'adjective', 'pronoun', 'preposition', 'adverb', 'conjunction',
              'phrasal verb', 'idiom', 'slang']

db.define_table('entry',
    Field('word', required=True, notnull=True),
    Field('category', required=True, requires=IS_IN_SET(categories), notnull=True),
    Field('meaning', required=True, notnull=True),
    Field('example'),
    Field('created', 'datetime', writable=False, readable=False, default=datetime.now())
)