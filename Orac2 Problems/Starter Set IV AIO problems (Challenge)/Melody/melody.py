import sys


data = list(map(int, sys.stdin.read().split()))
H, K = data[0:2]
notes = data[2:]
note1 = []
note2 = []
note3 = []
changes = 0
for i in range(0, len(notes), 3):
    note1.append(notes[i])
    note2.append(notes[i+1])
    note3.append(notes[i+2])
notes = [note1, note2, note3]
for note_group in notes:
    note_group_freq = {}
    if len(set(note_group)) == 1:
        continue
    else:
        for note in note_group:
            note_group_freq[note] = note_group_freq.get(note, 0) + 1
        changes += sum(note_group_freq.values()) - max(note_group_freq.values())

print(changes)



