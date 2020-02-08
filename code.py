"""
This script fetches the follower count from a Twitter account and display
it on a PyPortal.
"""
import board
import time

from adafruit_pyportal import PyPortal

# The username to check
USERNAME = "spaceboyr00"

# The URL for the Twitter data.
SOURCE = "https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names="+USERNAME

# The follower count.
FOLLOWER_COUNT = [0, "followers_count"]

# Where this file exists. We need this to locate fonts and images later.
cwd = ("/"+__file__).rsplit('/', 1)[0]

# Create a PyPortal object with specific parameters.
pyportal = PyPortal(url=SOURCE,
                    json_path=FOLLOWER_COUNT,
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/twitter_bg.bmp",
                    text_font=cwd+"/fonts/Collegiate-50.bdf",
                    text_position=(200, 240),
                    text_color=0xFFFFFF,
                    # Uncomment te following lines to show the Twitter 
                    # account url at the bottom of the display.
                    # caption_text="twitter.com/"+USERNAME,
                    # caption_font=cwd+"/fonts/Collegiate-24.bdf",
                    # caption_position=(110, 300),
                    # caption_color=0xFFFFFF,
                    )

# The main loop.
while True:
	# Try to get the Twitter data. If successful, it will update the
    # display to show the follower count.
    try:
        value = pyportal.fetch()
        print("Response is", value)
    # If we fail, print out the error.
    except (ValueError, RuntimeError) as e:
        print("An error occured. -", e)

    # Wait between checks. Change this to update faster or slower but try to
    # keep it above 60 seconds. In general, one hit to the Twitter API per
    # minute or greater is enough to keep them from getting angry at you.
    time.sleep(60)
