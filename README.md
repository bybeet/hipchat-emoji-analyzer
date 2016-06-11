# HipChat Emoji Analyzer

This is a utility to take the HipChat Export JSON and show some interesting numbers around emoji usage. Currently the following pieces of information are reported on:

 * Number of emojis used per user
 * Number of times an emoji is used
 * How many emojis are used throughout the day
 * Total number of emojis used

#Table of Contents
* [Usage](#usage)
* [HipChat JSON Export Format](#export-format)
* [TODO](#todo)


## Usage

### Process the files
Set `INPUT_DIR` in `process.py` to the directory that contains the HipChat export data. Every file will be read, and then a summary json will be created in `OUTPUT_DIR`. This operation can take a while depending on how much chat history you have, but will only need to be run once (unless additional chat files or output information is added).

### Output some information
Set `OUTPUT_DIR` and `OUTPUT_FILENAME` in `analyze.py`. Run the script and information will be printed out.

## Export Format
### Json Input Structure
```json
[
 {
    "date":"2016-03-17T13:59:11+0000",
    "from":{
       "name":"First Last",
       "user_id":650669
     },
     "message":"message contents"
    },
    ...
]
```

## TODO
- [ ] Graphs
- [ ] Whitelist/blacklist emojis and users
- [ ] Provide input/output dirs as program arg