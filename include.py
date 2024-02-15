import wikipediaapi

#prend un string et renvoit la page existante, si elle n'existe pas on lève une erreur
def getPage(pageName):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (arthurblamart@gmail.fr)', 'fr')
    page = wiki_wiki.page(pageName)
    if(not page.exists()):
       raise NameError(f"Page inexistante : {pageName}")
    return page

#Prend une page et renvoit une liste des pages liées
def getLinked(page):
    resList = [pages for pages in page.links.values()]
    return resList

#Prend deux pages et renvoit la distance entre les deux (-1 sinon)
def howLongFromAToB(pageA, pageB, profondeurMax):
    linked = getLinked(pageA)
    #Si la profondeur max est nulle alors on as aps trouvé
    if(profondeurMax==0):
        return -1
    else:
        #On regarde d'abord si la page à été trouvé (on ne veut pas explorer tous si c'est le cas)
        for page in linked:
            if(page.title == pageA.title):
                return 1
        #Si on as pas trouvé précédemment on appelle le récursif
        for page in linked:
            recRes = howLongFromAToB(pageA, page, profondeurMax-1)
            if recRes!=(-1):
                print(page.title)
                return 1+recRes
        #Si on a toujours rien trouvé
        return -1