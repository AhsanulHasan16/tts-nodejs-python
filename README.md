# tts-nodejs-python
This is just a short nodejs project. Used for TTS. Text to Speech.

I got the idea yesterday when in an interview, the interviewer asked me if we could execute Python scripts from node. And I said yes we can because I knew that there were ways. But what I did not know was, what the ways were. So after the interview, I decided to research about this a bit and build a quick short express application with Python. And the first thing that came to my mind about what to do with Python was TTS. I don't really know why but that was the first thing that came to my mind and so I started on this today and alhamdulillah I'm also done more or less. I have implemented everything I wanted to. And I'm feeling very good that I could do it without any issues. My node and express knowledge is better than I really thought! 

The only other thing that I want to add or modify rather, in this app is, using spawn instead of python-shell. Apparently, spawn is better at processing Python and it is faster with node.
So, the next thing to do in the project will be, to add and integrate spawn in place of python-shell.

After the TTS implementation, I was thinking if there were any enhancements that were possible to this app and then it hit me. We did TTS so how about now we do the opposite, STT?
STT was harder compared to TTS but I managed to implement it in the project. 

For easier testing, what I did was, first in the TTS API, I got a speech from an English text, and then after that, I just took that mp3 file of the output and uploaded it in the STT API. Pretty neat.


Not sure if I will be adding anything else in the project but there are some more ideas that are boiling inside of me. Maybe a bengali STT if I can? Let's see.

Another idea I have for this one is to make a mobile app out of it. Will need to take a look at react native. Won't be that much of a problem. In sha Allah!


Ok, so bengali STT is done! Hell yeah!

Though it looks like it's only a handful of lines of code but it took like a whole day to implement this thing. But I'm satisfied that I was able to achieve this today.


The next goal for this project is to make this one into a mobile app. I was thinking about learning react native and this will be the perfect opportunity to do that.

Not sure how much time that would take, but it will surely take a while. But I will achieve that too, in sha Allah!


- Saki
