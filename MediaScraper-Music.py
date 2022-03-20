from requests import get
import youtube_dl
song = input('Song Name: ')

headers = {'X-Requested-With': 'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 '
               'Safari/537.36',
            'Accept-Encoding': 'gzip, deflate, br',
           'Cookie': '_ga=GA1.2.1783348305.1647687088; _gid=GA1.2.889592270.1647687088',
           'Referer': 'https://slider.kz/',
           'Connection': 'keep-alive'
           }
count = 0
all_url = []
data = get(f'https://slider.kz/vk_auth.php?q={song.replace(" ", "%20")}', headers=headers).json()
for i in range((len(data['audios']['']))):
    count += 1
    print(f"[{count}] {data['audios'][''][i]['tit_art']}")
    all_url.append(f"https://slider.kz/download/{data['audios'][''][i]['id']}/{data['audios'][''][i]['duration']}/"
                   f"{data['audios'][''][i]['url']}/{str(data['audios'][''][i]['tit_art']).replace(' ', '%20')}"
                   f"/.mp3?extra=null")
number = int(input('Enter Number: '))
with youtube_dl.YoutubeDL({'outtmpl': data['audios'][''][number-1]['tit_art']}) as ydl:
    ydl.download([all_url[number-1]])
