ip_address = str(input('Please enter an I.P address: '))
originalL = len(ip_address)
newAddress = ''
for i in originalL:
    if ip_address[i] in '0123456789':
        newAddress = newAddress + ip_address[i]
newL = len(newAddress)
segments = (originalL - newL) + 1
print(segments)

# ipAddress = str(input("Please enter an IP address: "))
#
# segment = 1
# segment_length = 0
# character = ""
# for character in ipAddress:
#     if character == '.':
#         print("segment {} contains {} characters".format(segment, segment_length))
#         segment += 1
#         segment_length = 0
#     else:
#         segment_length += 1

