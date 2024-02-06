import icalendar
import re

with open('basic.ics', 'r') as handle:
    calendar = icalendar.Calendar.from_ical(handle.read())

CALENDARS = {
    'single-cell': [r'single.?cell'],
    'wg-systems': [r'Systems WG'],
    'sig-chairs': [r'Galaxy SiG Chairs'],
}

OUTPUTS = {k: [] for k in CALENDARS.keys()}

for event in calendar.walk('VEVENT'):
    for cal, matches in CALENDARS.items():
        for m in matches:
            if re.match(m, str(event['SUMMARY']), re.IGNORECASE):
                OUTPUTS[cal].append(event)

for k, events in OUTPUTS.items():
    header = f"""BEGIN:VCALENDAR
PRODID:-//Github Calendar Subset Exporter//hexylena 1.0//EN
VERSION:2.0
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Galaxy {k} Calendar
X-WR-TIMEZONE:UTC
X-WR-CALDESC:Subset of the official Galaxy Working Groups Calendar
"""

    with open(f"{k}.ics", 'w') as handle:
        handle.write(header)
        for event in events:
            handle.write(event.to_ical().decode('utf-8'))
        handle.write("END:VCALENDAR")
