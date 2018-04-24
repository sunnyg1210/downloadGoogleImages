from google_images_download import google_images_download as gmd

google = gmd.googleimagesdownload()

#####################
# EDIT THIS SECTION #
#####################

keywords = [
    {
        "word": "family gathering, indian family, chinese family",
        "limit": 20
    },{
        "word": "china technology, china artificial island, london architecture, railway, busy city",
        "limit": 20
    },{
        "word": "business meeting real, real office, computer warehouse, amazon warehouse",
        "limit": 20
    },{
        "word": "manhattan street, india street, china street, street food, scotland village",
        "limit": 30
    },{
        "word": "scottish highlands, scottish castles",
        "limit": 20
    },{
        "word": "new year",
        "limit": 10
    }
]

####################
# END EDIT SECTION #
####################

def downloadImages(keyword, limit):
    print('Started download for %s images using keyword "%s"' % (limit, keyword))
    args = {
        "keywords": keyword,
        "limit": limit,
        "print_urls": False,
        "related_images": False
    }
    google.download(args)
    print('Finished downloading - %s - images for keyword - "%s"' % (limit, keyword))
    
def job():
    for keyword in keywords:
        downloadImages(keyword['word'], keyword['limit'])
    print('ALL DONE :)')
    
job()
