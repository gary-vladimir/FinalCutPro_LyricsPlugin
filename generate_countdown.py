#!/usr/bin/env python3
"""
Simple FCPXML Generator for Final Cut Pro Countdown Timer
Creates 10 title elements numbered 1-10, each lasting 1 second.
"""

def generate_fcpxml():
    """Generate FCPXML with 10 sequential 1-second title clips."""

    # FCPXML header - simple and minimal
    xml = '''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE fcpxml>
<fcpxml version="1.10">
  <resources>
    <format id="r1" name="FFVideoFormat1080p30" frameDuration="1/30s" width="1920" height="1080"/>
    <effect id="r2" name="Basic Title" uid=".../Titles.localized/Bumper:Opener.localized/Basic Title.localized/Basic Title.moti"/>
  </resources>
  <library>
    <event name="Countdown Timer">
      <project name="Timer 1-10">
        <sequence format="r1" duration="10s" tcStart="0s" tcFormat="NDF">
          <spine>
'''

    # Generate 10 title elements with inline text styling
    for i in range(1, 11):
        offset = i - 1  # Start at 0 seconds
        xml += f'''            <title ref="r2" name="{i}" offset="{offset}s" duration="1s">
              <text>
                <text-style font="Helvetica" fontSize="96" fontFace="Regular" fontColor="1 1 1 1" alignment="center">{i}</text-style>
              </text>
            </title>
'''

    # FCPXML footer
    xml += '''          </spine>
        </sequence>
      </project>
    </event>
  </library>
</fcpxml>
'''

    return xml


def main():
    """Main function to generate and save FCPXML file."""

    # Generate the XML content
    fcpxml_content = generate_fcpxml()

    # Output filename
    output_file = "countdown.fcpxml"

    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fcpxml_content)

    print(f"✓ Generated: {output_file}")
    print(f"✓ Contains: 10 title clips (1-10), each 1 second")
    print(f"\nNext steps:")
    print(f"1. Open Final Cut Pro")
    print(f"2. Go to File > Import > XML")
    print(f"3. Select '{output_file}'")
    print(f"4. The countdown timer will appear in your library!")


if __name__ == "__main__":
    main()
