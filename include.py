import wikipediaapi

#prend un string et renvoit la page existante, si elle n'existe pas on lève une erreur
def getPage(pageName):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (arthurblamart@gmail.fr)', 'fr')
    page = wiki_wiki.page(pageName)
    print(pageName)
    if(not page.exists()):
       raise NameError(f"Page inexistante : {pageName}")
    return page

#Prend une page et renvoit une liste des pages liées
def getLinked(page):
    resList = [pages for pages in page.links.values()]
    return resList