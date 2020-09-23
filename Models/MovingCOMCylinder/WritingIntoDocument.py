# File is written from the beginig evrytime, so stuff is replaced, whole file is replaced
text_file = open("NewModel.urdf", "w")
n = text_file.write('Line 1\n')
text_file.close()

text_file = open("NewModel.urdf", "w")
n = text_file.write('Line 2\n')
n = text_file.write('Line 2\n')
text_file.close()

text_file = open("NewModel.urdf", "w")
n = text_file.write('Line 3\n')
text_file.close()