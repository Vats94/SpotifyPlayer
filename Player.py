import spotipy
import time
from gpiozero import Button
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(rs=26, en=19, d4=13, d5=6, d6=5, d7=11, cols=16, lines=2)

forward = Button(4)
pause_play = Button(3)
pause_play_bool = False
back = Button(2)

username = ''
cid = ''
cs = ''
ruri = "http://localhost:8888"

scope = 'user-read-currently-playing user-read-playback-state user-modify-playback-state streaming'
token = spotipy.util.prompt_for_user_token(username, scope, cid, cs, ruri)

def ms_convert(ms):
    seconds = (ms / 1000) % 60
    minutes = (ms / (1000 * 60)) % 60

    if(seconds < 10):
        seconds = '0' + str(int(seconds))
    else:
        seconds = str(int(seconds))

    return str(int(minutes)) + ':' + seconds


sp = spotipy.Spotify(auth=token)

while(True):

    current_song = sp.current_user_playing_track()
    artist = current_song['item']['artists'][0]['name']
    song_name = current_song['item']['name']
    progress_ms = current_song['progress_ms']

    id = current_song['item']['id']
    track = sp.track(id)
    duration = track['duration_ms']

    #lcd.message(song_name,'-',artist, ms_convert(progress_ms), ms_convert(duration))


    time.sleep(1)

    a = sp.devices()

    i=0

    while(i < len(a['devices'])):
        if (a['devices'][i]['is_active'] == True):
            device_id = a['devices'][i]['id']
        i+=1
        
    if(pause_play.is_pressed):
        try:
            sp.pause_playback(device_id)
        except:
            sp.start_playback(device_id)
        
    if(forward.is_pressed):
        sp.next_track(device_id)
    
    if(back.is_pressed):
        sp.previous_track(device_id)
    
