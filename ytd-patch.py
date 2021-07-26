import os
import re
import datetime as dt

today = dt.datetime.now().date()
# directory = os.getcwd()
directory = r'C:\Users\Jeremiah\Downloads\youtube-dl'

with open('criteria.txt', 'r') as file:
    condition = file.read().splitlines()
    condition.sort(key=len, reverse=True)

x = 0
for song in os.listdir(directory):
    os.chdir(directory)
    filetime = dt.datetime.fromtimestamp(os.path.getctime(song))
    old_song_name = song
    if filetime.date() == today and song.endswith(".wav"):
        song = song.lower()
        for item in condition:
            item = item.lower()
            if song.find(item) >= 0:
                x += 1
                new_song = re.compile(re.escape(item), re.IGNORECASE)
                new_song = new_song.sub('', old_song_name)
                new_song = new_song.replace(
                    '[]', '').replace('()', '').replace('{}', '').replace('  ', ' ').replace(
                    ' .wav', '.wav')
                print(new_song)
                os.rename(old_song_name, new_song)
                break
print('{} songs patched'.format(x))