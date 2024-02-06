import icalendar
import re

with open('basic.ics', 'r') as handle:
    calendar = icalendar.Calendar.from_ical(handle.read())

CALENDARS = {
    'single-cell': [r'single.?cell'],
    'wg-systems': [r'Systems WG']
}

OUTPUTS = {k: [] for k in CALENDARS.keys()}

for event in calendar.walk('VEVENT'):
    for cal, matches in CALENDARS.items():
        for m in matches:
            if re.match(m, str(event['SUMMARY']), re.IGNORECASE):
                OUTPUTS[cal].append(event)


for k, events in OUTPUTS.items():
    with open(f"{k}.ics", 'w') as handle:
        for event in events:
            handle.write(event.to_ical().decode('utf-8'))
