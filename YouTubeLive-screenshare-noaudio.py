#!/usr/bin/env python
"""
https://www.scivision.co/youtube-live-ffmpeg-livestream/

Cross-platform live streaming to YouTube Live using FFmpeg

this is alpha testing script
"""
import subprocess as S
from getpass import getpass

try:
    ret = S.check_call(('ffmpeg','-h'), stdout=S.DEVNULL)
except S.CalledProcessError:
    raise FileNotFoundError('FFmpeg is not installed for your system.')

streamfps = 10
res = '1024x720'
origin = ':0.0+0,24'
group=20
bufsize='512k'

vid =  ('-f', 'x11grab','-r',str(streamfps),'-s',res,'-i',origin,
       '-vcodec','libx264','-pix_fmt','yuv420p','-preset','ultrafast','-g',str(group))

codec = ('-threads','0','-bufsize',bufsize,
        '-f','flv')



cmd = ('ffmpeg',) + vid + codec
print(cmd)

ret = S.run(cmd+('rtmp://a.rtmp.youtube.com/live2/'+getpass('YouTube Live Stream ID: '),),stdout=S.DEVNULL)