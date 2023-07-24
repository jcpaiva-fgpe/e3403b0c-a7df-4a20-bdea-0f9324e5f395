from re import split
txt="""Rozdział I
Historia się zaczyna. Tu nic się nie dzieje. Ale jest to fajnie opisane.
Rozdział II
Historia się rozwija. Tu też nic się nie dzieje. Ale jest to bardzo fajnie opisane.
Rozdział III
Historia się kończy. Tu już zupełnie nic się nie dzieje. Ale nawet to jest fajnie opisane."""
print(split(r"Rozdział I+\n", txt)[1:])
