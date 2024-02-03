import wikipediaapi

def getPage(pageName):
    wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'fr')
    page = wiki_wiki.page(pageName)
    if(not page.exists()):
       raise NameError(f"Page inexistante : {pageName}")
    return page