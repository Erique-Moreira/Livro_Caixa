# -*- coding: utf-8 -*-
@auth.requires_login()
def cad_gast():
    return dict()

@auth.requires_login()
def aluguel():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        print a
        x = db.livro[a]
        alug = x.aluguel
    formulario = SQLFORM.factory(Field('aluguel', 'float', label = 'Aluguel R$ : '), )
    if formulario.process().accepted:
        alu = float(formulario.vars.aluguel)
        alug = alu + alug
        print alug
        db(db.livro.data == mes+" de "+ano).update(aluguel=alug)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

@auth.requires_login()
def auxiliar():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        print a
        x = db.livro[a]
        auxil = x.auxiliar
    formulario = SQLFORM.factory(Field('auxiliar', 'float', label = 'Auxiliar R$ : '), )
    if formulario.process().accepted:
        aux = float(formulario.vars.auxiliar)
        auxil = aux + auxil
        db(db.livro.data == mes+" de "+ano).update(auxiliar=auxil)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

@auth.requires_login()
def dental():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        print a
        x = db.livro[a]
        dent = x.dental
    formulario = SQLFORM.factory(Field('dental', 'float', label = 'Dental R$ : '), )
    if formulario.process().accepted:
        den = float(formulario.vars.dental)
        dent = den + dent
        db(db.livro.data == mes+" de "+ano).update(dental=dent)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def agua():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        print a
        x = db.livro[a]
        agu = x.agua
    formulario = SQLFORM.factory(Field('agua', 'float', label = 'Água R$ : '), )
    if formulario.process().accepted:
        ag = float(formulario.vars.agua)
        agu = ag + agu
        db(db.livro.data == mes+" de "+ano).update(aluguel=agu)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def luz():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        print a
        x = db.livro[a]
        lu = x.luz
    formulario = SQLFORM.factory(Field('luz', 'float', label = 'Energia Elétrica R$ : '), )
    if formulario.process().accepted:
        l = float(formulario.vars.luz)
        lu = l + lu
        db(db.livro.data == mes+" de "+ano).update(luz=lu)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def lixo():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        lix = x.lixo
    formulario = SQLFORM.factory(Field('lixo', 'float', label = 'Lixo Hospitalar R$ : '), )
    if formulario.process().accepted:
        li = float(formulario.vars.lixo)
        lix = li + lix
        db(db.livro.data == mes+" de "+ano).update(lixo=lix)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def protetico():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        prot = x.protetico
    formulario = SQLFORM.factory(Field('protetico', 'float', label = 'Protético R$ : '), )
    if formulario.process().accepted:
        pro = float(formulario.vars.protetico)
        prot = pro + prot
        db(db.livro.data == mes+" de "+ano).update(protetico=prot)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def impostos():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        impo = x.impostos
    formulario = SQLFORM.factory(Field('impostos', 'float', label = 'Impostos e Taxas R$ : '), )
    if formulario.process().accepted:
        imp = float(formulario.vars.impostos)
        impo = imp + impo
        db(db.livro.data == mes+" de "+ano).update(impostos=impo)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def taxas():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        taxa = x.taxas
    formulario = SQLFORM.factory(Field('taxas', 'float', label = 'Taxas Bancárias R$ : '), )
    if formulario.process().accepted:
        tax = float(formulario.vars.taxas)
        taxa = tax + taxa
        db(db.livro.data == mes+" de "+ano).update(taxas=taxa)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def papelaria():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        papel = x.papelaria
    formulario = SQLFORM.factory(Field('papelaria', 'float', label = 'Papelaria R$ : '), )
    if formulario.process().accepted:
        pap = float(formulario.vars.papelaria)
        papel = pap + papel
        db(db.livro.data == mes+" de "+ano).update(papelaria=pap)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def manutencao():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        manu = x.manutencao
    formulario = SQLFORM.factory(Field('manutencao', 'float', label = 'Manutencao R$ : '), )
    if formulario.process().accepted:
        man = float(formulario.vars.manutencao)
        manu = man + manu
        db(db.livro.data == mes+" de "+ano).update(manutencao=manu)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def distribuidora():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        dist = x.distribuidora
    formulario = SQLFORM.factory(Field('distribuidora', 'float', label = 'Distribuidora R$ : '), )
    if formulario.process().accepted:
        dis = float(formulario.vars.distribuidora)
        dist = dis + dist
        db(db.livro.data == mes+" de "+ano).update(distribuidora=dist)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def telefone():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        y = x.telefone
    formulario = SQLFORM.factory(Field('telefone', 'float', label = 'Telefone R$ : '), )
    if formulario.process().accepted:
        z = float(formulario.vars.telefone)
        y = z + y
        db(db.livro.data == mes+" de "+ano).update(distribuidora=y)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def fgts():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        y = x.fgts
    formulario = SQLFORM.factory(Field('fgts', 'float', label = 'FGTS R$ : '), )
    if formulario.process().accepted:
        z = float(formulario.vars.fgts)
        y = z + y
        db(db.livro.data == mes+" de "+ano).update(fgts=y)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def inss():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        y = x.inss
    formulario = SQLFORM.factory(Field('inss', 'float', label = 'INSS R$ : '), )
    if formulario.process().accepted:
        z = float(formulario.vars.inss)
        y = z + y
        db(db.livro.data == mes+" de "+ano).update(inss=y)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def marketing():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        y = x.marketing
    formulario = SQLFORM.factory(Field('marketing', 'float', label = 'Marketing R$ : '), )
    if formulario.process().accepted:
        z = float(formulario.vars.marketing)
        y = z + y
        db(db.livro.data == mes+" de "+ano).update(marketing=y)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)

def outros():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        a = rows.id
        x = db.livro[a]
        y = x.outros
    formulario = SQLFORM.factory(Field('outros', 'float', label = 'Outros R$ : '), )
    if formulario.process().accepted:
        z = float(formulario.vars.outros)
        y = z + y
        db(db.livro.data == mes+" de "+ano).update(outros=y)
        redirect(URL('cad_gast'))
    return dict(formulario=formulario)
