# -*- coding: utf-8 -*-

def create():
    word = request.vars['word']
    category = request.vars['category']
    meaning = request.vars['meaning']
    example = request.vars['example']
    if db.word_index.insert(word=word, category=category, meaning=meaning, example=example):
        return dict(sucess=True)
    return dict(success=False)

def delete():
    dict_id = request.args(0)
    if db.word_index[dict_id]:
        del db.word_index[dict_id]
        return dict(success=True)
    return dict(success=False)

def update():
    return dict()

def read():
    dict_id = request.args(0)
    entry = db.word_index[dict_id]
    return dict(entry=entry)
