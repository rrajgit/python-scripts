# https://cdn.cs50.net/mobile/2018/spring/lectures/0/lang/en/lecture0.srt
import wget

for i in range(13):
  wget.download("https://cdn.cs50.net/mobile/2018/spring/lectures/{}/lang/en/lecture{}.srt".format(i, i))

#for i in range(11, 28):
#  wget.download("https://web.stanford.edu/class/archive/cs/cs103/cs103.1184/lectures/{}/Slides{}.pdf".format(i, i))
