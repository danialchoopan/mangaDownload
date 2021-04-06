import requests
import time
import os

counterMangaImg=0
counterMangaChapter=1

while True:
    downloadUrl='url/{mangaChapter}/{mangaImg}.jpg'
    

    while True:
        strDownload=downloadUrl.format(mangaChapter=counterMangaChapter,mangaImg=counterMangaImg)
        print(strDownload)
        downloadRequest=requests.get(strDownload,allow_redirects=True)
        if(downloadRequest.status_code==200):
            if not os.path.exists(str(counterMangaChapter)):
                os.mkdir(str(counterMangaChapter))
            open('{downloadChapter}/{counterMangaImg}.jpg'.format(downloadChapter=counterMangaChapter,counterMangaImg=counterMangaImg),'wb').write(downloadRequest.content)
        else:
            counterMangaImg=1
            counterMangaChapter=counterMangaChapter+1
            continue

        if counterMangaImg==300:
            counterMangaImg=1
            break
        counterMangaImg=counterMangaImg+1

    if counterMangaChapter>300:
        break

    counterMangaChapter=counterMangaChapter+1

