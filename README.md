# minecraftHeartsDetector
Here's a little something that'll add some zest to your socks.

This code is designed to work specifically on Windows machines, it can be tweaked to work on Linux and Apple.

If you're planning to use this with a taser or anything else that could hurt you make sure to have Minecraft open and ready, After running you'll have 5 seconds to get the hearts up on screen before the fun starts. (Update "time.sleep()" to increase or decrease this delay)

Within "Function to capture screenshots" you may need to adjust w and h.
Currently they capture a box that wraps around the hearts so less data gets processed but this may be different on different systems.

A couple lines below that you'll see " cDC.BitBlt((0,0), (w, h) , dcObj, (480,630), win32con.SRCCOPY)" adjust the 480, 630 to add or reduce bottom and left margin.

Lastly, the bottom of the code you'll see alot of "cv.imshow(,)" commented out.
If you're interested in how the end product is accomplished un-comment these to see.
If you're not horney for code donet worry about it.


Any projects you end up using this code for please tag me in them, I'd love to see what gets created.

Happy zapping.
