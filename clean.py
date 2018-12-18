
with open("uncut.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] 

cleanText = ""
count = 0
prev = 1045
for line in content:
	cleanLine = line.split("+++$+++")

	if prev - 1 == int((cleanLine[0].strip().replace("L", ""))):
		prev -= 1
	else:
		cleanText += "*\n"
		prev = int((cleanLine[0].strip().replace("L", "")))

	if len(cleanLine) == 5:

		if count % 2 == 0:
			cleanText += "-"
		else:
			cleanText += "--"

		cleanText += cleanLine[-1].strip() + "\n"

		count += 1


f = open("cut.txt", "a")
f.write(unicode(cleanText, errors='ignore'))

