# PomoHelper
Automated focus assistant for practicing the Pomodoro technique

Essentially, the Firefox session's JSON file (located in the %AppData% folder) is monitored to identify the current tab along with its respective URL.

Once this information is obtained, a comparison is made between the URL and those of YouTube and Facebook. In the case of a positive match, a set of keyboard commands (Ctrl + F4) is sent, closing the current tab in Firefox.

The entire process of extracting current data and performing comparisons is enclosed within a loop that only terminates after 20 minutes. This termination is based on comparing the start time of the code execution with the current time in each iteration of the main loop.
