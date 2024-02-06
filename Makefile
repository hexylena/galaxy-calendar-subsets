all: basic.ics
	python export.py

basic.ics:
	wget https://calendar.google.com/calendar/ical/5l6o0msfduoir59hrab0jlkocc%40group.calendar.google.com/public/basic.ics -O basic.ics
