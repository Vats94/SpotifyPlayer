from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.led_matrix.device import max7219
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
import spotipy
import random
import time

username = 'therime94'
cid = 'b48acb6c95dd4e338628ae588b8c919d'
cs = 'd5de6abe3adf4ef190e23db35a34ec5f'
ruri = "http://localhost:8888"

scope = 'user-read-currently-playing user-read-playback-state user-modify-playback-state streaming'
token = spotipy.util.prompt_for_user_token(username, scope, cid, cs, ruri)
sp = spotipy.Spotify(auth=token)

width = 32
height = 8

serial = spi(port = 0, device = 0, gpio = noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)

def draw_point(x,y):
    with canvas(device) as draw:
        draw.point((x,y), 'white')
        
def draw_line(x,y,z,q):
    with canvas(device) as draw:
        draw.line( (x,y,z,q), fill = 'white'  )
        
def ms_convert(ms):
    seconds = (ms / 1000) % 60
    minutes = (ms / (1000 * 60)) % 60

    if(seconds < 10):
        seconds = '0' + str(int(seconds))
    else:
        seconds = str(int(seconds))

    return str(int(minutes)) + ':' + seconds      
        
current_song = sp.current_user_playing_track()
artist = current_song['item']['artists'][0]['name']
song_name = current_song['item']['name']
progress_ms = current_song['progress_ms']

id = current_song['item']['id']
track = sp.track(id)
duration = track['duration_ms']

print(song_name,'-',artist, ms_convert(progress_ms), ms_convert(duration))

m = []

for j in range(0,32):
    m.append(random.randint(0,7))

for y in range(0,100000):
    for x in range(0,32):
        draw_line(0,m[0], 0, height)
        draw_line(1,m[1], 1, height)
        draw_line(2,m[2], 2, height)
        draw_line(3,m[3], 3, height)
        draw_line(4,m[4], 4, height)
        draw_line(5,m[5], 5, height)
        draw_line(6,m[6], 6, height)
        draw_line(7,m[7], 7, height)
        draw_line(8,m[8], 8, height)
        draw_line(9,m[9], 9, height)
        draw_line(10,m[10], 10, height)
        draw_line(11,m[11], 11, height)
        draw_line(12,m[12], 12, height)
        draw_line(13,m[13], 13, height)
        draw_line(14,m[14], 14, height)
        draw_line(15,m[15], 15, height)
        draw_line(16,m[16], 16, height)
        draw_line(17,m[17], 17, height)
        draw_line(18,m[18], 18, height)
        draw_line(19,m[19], 19, height)
        draw_line(20,m[20], 20, height)
        draw_line(21,m[21], 21, height)
        draw_line(22,m[22], 22, height)
        draw_line(23,m[23], 23, height)
        draw_line(24,m[24], 24, height)
        draw_line(25,m[25], 25, height)
        draw_line(26,m[26], 26, height)
        draw_line(27,m[27], 27, height)
        draw_line(28,m[28], 28, height)
        draw_line(29,m[29], 29, height)
        draw_line(30,m[30], 30, height)
        draw_line(31,m[31], 31, height)
        m.pop(0)
        m.append(random.randint(0,7))        
        
