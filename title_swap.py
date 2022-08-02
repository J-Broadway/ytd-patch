import os
import csv
import time
import datetime as dt
import numpy as np


swap_csv = r"C:\Users\Jeremiah\Python\Scripts\User\ytd-patch\swap_temp.csv"
directory = r'C:\Users\Jeremiah\Downloads\youtube-dl'


# Check if swap_temp.csv is older than 1 day.
def is_file_older_than_x_days(file, days=1):
    file_time = os.path.getmtime(file)
    return (time.time() - file_time) / 3600 > 24*days


def main():
    os.chdir(directory)
    matches = [" ft. ", " feat. ", " featuring "]
    today = dt.datetime.now().date()
    song_list = []
    i = 0

    if is_file_older_than_x_days(swap_csv) is True:
        os.remove(swap_csv)
        # Create empty CSV file
        with open(r"C:\Users\Jeremiah\Python\Scripts\User\ytd-patch\swap_temp.csv", "w"):
            pass

    for file in os.listdir():
        filetime = dt.datetime.fromtimestamp(os.path.getctime(file))
        file_name, file_ext = os.path.splitext(file)
        loop_breakout = 0

        if file_ext == ".wav" and filetime.date() == today:

            # Check if song has already been swapped
            with open(swap_csv) as f:
                csvread = csv.reader(f, delimiter="\n")
                for item in csvread:
                    if item[0] == file:
                        loop_breakout = 1
            if loop_breakout == 1:
                break
            if file_name.find(" - ") > 0:
                # Defining Metadata
                file_name = file_name.split(" - ")
                artist = file_name[0]
                song_name = file_name[1]

                for x in matches:
                    if song_name.find(x) > 0:
                        song_name, features = song_name.split(x)
                        new_name = "{0} - {1} (ft. {2}){3}".format(song_name, artist, features, file_ext)
                        os.rename(file, new_name)
                        song_list.append(new_name)
                        i += 1
                        break
                    elif song_name.find(x) == -1:
                        new_name = ("{0} - {1}{2}".format(song_name, artist, file_ext))
                        os.rename(file, new_name)
                        song_list.append(new_name)
                        i += 1
                        break

    # If song list is not empty append to csv
    if len(song_list):
        song_list = np.array(song_list)
        np.savetxt(swap_csv, song_list, fmt="%s")
    print("{} titles swapped".format(i))
main()
