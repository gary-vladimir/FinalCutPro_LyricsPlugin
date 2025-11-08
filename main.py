#!/usr/bin/env python3
"""
FCPXML Generator for Final Cut Pro - Lyrics Plugin
Reads lyrics from lyrics.json and generates FCPXML with timed title elements.
"""

import json


def snap_to_frame(time_seconds, fps=30):
    """Snap a time value to the nearest frame boundary and return as rational."""
    frames = round(time_seconds * fps)
    return frames, fps  # Return numerator and denominator


def generate_fcpxml(lyrics_data):
    """Generate FCPXML with title clips for each word from lyrics.json."""

    # Calculate total duration from the last word's end time
    total_duration = 0
    word_count = 0
    for segment in lyrics_data["segments"]:
        for word_data in segment["words"]:
            total_duration = max(total_duration, word_data["end"])
            word_count += 1

    # Snap total duration to frame boundary
    total_frames, fps = snap_to_frame(total_duration)
    total_duration_str = f"{total_frames}/{fps}s"

    # FCPXML header
    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.10">
  <resources>
    <format id="r1" name="FFVideoFormat1080p30" frameDuration="1/30s" width="1920" height="1080"/>
    <effect id="r2" name="Basic Title" uid=".../Titles.localized/Bumper:Opener.localized/Basic Title.localized/Basic Title.moti"/>
  </resources>
  <library>
    <event name="Lyrics">
      <project name="Song Lyrics">
        <sequence format="r1" duration="{total_duration_str}" tcStart="0s" tcFormat="NDF">
          <spine>
'''

    # Generate title elements for each word in the segments
    title_index = 1
    for segment in lyrics_data["segments"]:
        for word_data in segment["words"]:
            word = word_data["word"]
            start_frames, fps = snap_to_frame(word_data["start"])
            end_frames, fps = snap_to_frame(word_data["end"])
            duration_frames = end_frames - start_frames

            # Format as rational numbers
            offset_str = f"{start_frames}/{fps}s"
            duration_str = f"{duration_frames}/{fps}s"

            ts_id = f"ts{title_index}"

            xml += f'''            <title ref="r2" name="{word}" offset="{offset_str}" duration="{duration_str}">
              <text>
                <text-style ref="{ts_id}">{word}</text-style>
              </text>
              <text-style-def id="{ts_id}">
                <text-style font="Coolvetica" fontSize="80" fontFace="Regular" fontColor="1 1 1 1" bold="1" alignment="center"/>
              </text-style-def>
            </title>
'''
            title_index += 1

    # FCPXML footer
    xml += '''          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''

    return xml, word_count, total_frames / fps


def main():
    """Main function to read lyrics and generate FCPXML file."""

    # Read lyrics from JSON file
    lyrics_file = "lyrics.json"

    with open(lyrics_file, 'r', encoding='utf-8') as f:
        lyrics_data = json.load(f)

    # Generate the XML content
    fcpxml_content, word_count, total_duration = generate_fcpxml(lyrics_data)

    # Output filename
    output_file = "lyrics.fcpxml"

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fcpxml_content)

    print(f"✓ Generated: {output_file}")
    print(f"✓ Contains: {word_count} lyric title clips")
    print(f"✓ Total duration: {total_duration:.2f} seconds")
    print(f"\nNext steps:")
    print(f"1. Open Final Cut Pro")
    print(f"2. Go to File > Import > XML")
    print(f"3. Select '{output_file}'")
    print(f"4. The lyrics will appear on your timeline!")


if __name__ == "__main__":
    main()
