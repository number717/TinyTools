
f = file("new stories.txt")
data = f.read().split('\n')
f.close()

newdata = ','.join(data)
formatStory = file("format Story.txt", 'w')
formatStory.write(newdata)
formatStory.close