from sys import stdin

# If you export the timeline to a CSV with FCPX using command post
# Use this script to convert it to Chapters text for the description
# python3 chapter_maker.py < Episode\ 1\ -\ Pilot/Renders/Timeline\ Index.csv > test.txt

def build_entry_from_raw(arr):
    if len(arr) != 3: return

    first_item = arr[0].replace('"', '').replace("'", '')
    second_item = arr[1].replace('"', '').replace("'", '')

    second_item = ':'.join(second_item.split(':')[:-1])

    return f"{second_item} {first_item}"

# Main for the file
if __name__ == '__main__':
    # Make a list to hold each entry
    chapter_entries = []
    # Read in each line
    for line in stdin:
        # Break if EOF
        if line == '':
            break
        # Split the line up into into an entry array
        raw_entry = line.split('","')
        # Each entry will have 3 items :: "Name","Position","Notes"
        # Build a chapter_entry and add to list
        entry = build_entry_from_raw(raw_entry)
        chapter_entries.append(entry)

        if entry is None: print(raw_entry)

    # Remove the first line entry since it has no data in it
    del chapter_entries[0]

    # Write the first line
    print("Chapters:") 
    # Write each line to a text file
    for entry in chapter_entries:
        if entry is not None: print(entry)
    