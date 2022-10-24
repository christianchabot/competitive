from random import randint

playlist = [
    "White Room - Cream",
    "Escape (The Pina Colada Song) - Rupert Holmes",
    "Devil Like Me - Rainbow Kitten Suprise"
]

queue = []
for s in range(len(playlist)):
    found = False
    while not found:
        song = playlist[randint(0, len(playlist)-1)]
        found = song not in queue
    playlist.remove(song)
    queue.append(song)

print(queue)
