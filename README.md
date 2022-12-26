# VidCap

Generates closed caption for a video.

## Getting started
A very simple python script records the timestamp for each caption by simply tapping
the ``enter`` key.

### Step 1
create a input text file with ``.txt`` extension.
The first line should contain:
* Time (mm:ss) when first caption will show. 
* Length of the video (mm:ss).
Following lines will have one caption per line 

Example ``cafe1.txt``,
```
00:14  01:45
pondering on the balcony in a lazy afternoon
a cup of tea would be perfect now
walking along the path by the river
heading towards the local cafe
```
### Step 2
Arrange your desktop such that the python console and your video player like
**VLC** or **Movies & TV** or whatever you use (even **youTube**) are both visible and do not
overlap each other.

### Step 3
Run the script from your python console,
```
python --file cafe1.txt
```
Now the script will show the cue, is armed and waiting for your tap.


### Step 4
At this point you start playing the your video with your video player.

### Step 5
Go back to the python console and wait till when video comes to the
point when first caption will show.

Tap the ``enter key``. Then next cue will show. Wait till the video comes
to that point. Tap the ``enter key`` again. Keep repeating this process till
the timestamp for all the cues are recorded.

### Step 6
At this point, the script will generate subtitles in two formats,
* ``.lrc`` format
* ``.srt`` format

Now you can use them with wherever you need them like for **youTube** or something.

## Custom cue
Sometimes to provide custom hints like video imagery as a cue instead of showing the part
of the subtitle. In which case you can put the hint as shown below in the file.

Example ``cafe2.txt``,
```
00:14  01:45
balcony|pondering on the balcony in a lazy afternoon
tea|a cup of tea would be perfect now
walking|walking along the path by the river
cafe|heading towards the local cafe
```

## Reaction time
When you are tapping there might be a reaction delay. In which case the timestamp
will lag the video.

The script also saves the tap data in a ``.pkl`` file. You can use that file and regenerate the subtitles with delay compensation. For instance you are lagging by 5 seconds then to subtract 5 seconds from each timestamp simply run,

```
python --file cafe1.pkl --comp -5
```

The subtitles will be regenerated. You can also use this to do reverse compensation by providing a positive number.

Have fun subtitling!

## Unicode language support
If you are making subtitle in a language that does use english characters be aware that some consoles are retarded in terms of
font support for some languages. If you experience this,
simply use the custom cue with a language 
that console can properly display. In my case
I always use custom cue in english no matter
what language the subtitle is in.
