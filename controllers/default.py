# -*- coding: utf-8 -*-



@auth.requires_login()
def index():
    if db(db.livro.data == mes+" de "+ano).isempty():   
        db.livro.insert(data=mes+" de "+ano)
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        ler = rows.id
        x = db.livro[ler]
        
        a = x.aluguel
        b = x.dental
        c = x.auxiliar
        d = x.agua
        e = x.luz
        f = x.lixo
        g = x.protetico
        h = x.manutencao
        i = x.papelaria
        j = x.distribuidora
        k = x.impostos
        l = x.telefone
        m = x.taxas
        n = x.fgts
        o = x.inss
        p = x.marketing
        q = x.outros
        r = x.entrada1
        s = x.entrada2
        t = x.entrada3
        g_tot = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q)
        e_tot = (r + s+ t)
        saldo = (e_tot - g_tot)
        c_hora = (g_tot/210)

    return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, q=q, r=r, s=s, t=t,g_tot = g_tot, e_tot = e_tot, saldo=saldo, c_hora=c_hora,)


@auth.requires_login()
def relat():
    for rows in db(db.livro.data == mes+" de "+ano).select(db.livro.id):
        ler = rows.id
        x = db.livro[ler]
        
        a = x.aluguel
        b = x.dental
        c = x.auxiliar
        d = x.agua
        e = x.luz
        f = x.lixo
        g = x.protetico
        h = x.manutencao
        i = x.papelaria
        j = x.distribuidora
        k = x.impostos
        l = x.telefone
        m = x.taxas
        n = x.fgts
        o = x.inss
        p = x.marketing
        q = x.outros
        r = x.entrada1
        s = x.entrada2
        t = x.entrada3
        g_tot = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q)
        e_tot = (r + s+ t)
        saldo = (e_tot - g_tot)
        c_hora = (g_tot/210)

    return dict(a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, q=q, r=r, s=s, t=t,g_tot = g_tot, e_tot = e_tot, saldo=saldo, c_hora=c_hora,)

@auth.requires_login()
def relat_ant():
    return dict()

def relat_res():
    id_res = request.args(0)
    
    
    for rows in db(db.livro.id == id_res).select(db.livro.id):
        ler = rows.id
        data = "Data"
        x = db.livro[ler]
        y = x.data
        
        a = x.aluguel
        b = x.dental
        c = x.auxiliar
        d = x.agua
        e = x.luz
        f = x.lixo
        g = x.protetico
        h = x.manutencao
        i = x.papelaria
        j = x.distribuidora
        k = x.impostos
        l = x.telefone
        m = x.taxas
        n = x.fgts
        o = x.inss
        p = x.marketing
        q = x.outros
        r = x.entrada1
        s = x.entrada2
        t = x.entrada3
        g_tot = (a+b+c+d+e+f+g+h+i+j+k+l+m+n+o+p+q)
        e_tot = (r + s+ t)
        saldo = (e_tot - g_tot)
        c_hora = (g_tot/210)

    return dict(y=y, a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j, k=k, l=l, m=m, n=n, o=o, p=p, q=q, r=r, s=s, t=t,g_tot = g_tot, e_tot = e_tot, saldo=saldo, c_hora=c_hora,)
    
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
