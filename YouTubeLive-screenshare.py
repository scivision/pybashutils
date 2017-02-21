#!/usr/bin/env python
"""
Cross-platform live streaming to YouTube Live using FFmpeg

this is alpha testing script

https://www.scivision.co/youtube-live-ffmpeg-livestream/
"""
import subprocess as S
from getpass import getpass

try:
    S.check_call(('ffmpeg','-h'), stdout=S.DEVNULL)
except S.CalledProcessError:
    raise FileNotFoundError('FFmpeg is not installed for your system.')

streamfps = 10
res = '1024x720'
origin = ':0.0+0,24'
group=20
bufsize='512k'

audiochan = 'hw:1,0'
Nchan = '1'

def youtubelive(useaudio=False):

    vid1 = ('-f', 'x11grab',
            '-r',str(streamfps),'-s',res,'-i',origin)

    vid2 = ('-vcodec','libx264','-pix_fmt','yuv420p',
            '-preset','ultrafast','-g',str(group))

    if useaudio:
        aud1 = ('-f','alsa','-ac',Nchan,'-i',audiochan)
        aud2 = ('-acodec','libmp3lame','-ar','44100' )
    else:
        aud1 = aud2 = ()

    codec = ('-threads','0','-bufsize',bufsize,
            '-f','flv')



    cmd = ('ffmpeg',) + vid1 + aud1 + vid2 + aud2 + codec

    print(cmd)

    S.run(cmd+('rtmp://a.rtmp.youtube.com/live2/'+getpass('YouTube Live Stream ID: '),),
                stdout=S.DEVNULL)

if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('--audio',help='stream audio',action='store_true')
    p = p.parse_args()

    youtubelive(p.audio)