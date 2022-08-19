from random import randint as rnd

memReg = 'members.txt'
exReg = 'inactive.txt'
fee = ('yes', 'no')

# Generate a random member list


def genFiles(current, old):
    with open(current, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"

        for rowno in range(20):
            date = str(rnd(2015, 2020)) + '-' + \
                str(rnd(1, 12))+'-'+str(rnd(1, 25))
            writefile.write(data.format(
                rnd(10000, 99999), date, fee[rnd(0, 1)]))

    with open(old, 'w+') as writefile:
        writefile.write('Membership No  Date Joined  Active  \n')
        data = "{:^13}  {:<11}  {:<6}\n"
        for rowno in range(3):
            date = str(rnd(2015, 2020)) + '-' + \
                str(rnd(1, 12))+'-'+str(rnd(1, 25))
            writefile.write(data.format(rnd(10000, 99999), date, fee[1]))


genFiles(memReg, exReg)

# Clean the inactive users from the random member list


def cleanFiles(currentMem, exMem):
    with open(currentMem, "+r") as filetowrite:
        with open(exMem, "+a") as filetoappend:
            # get the data
            filetowrite.seek(0)
            members = filetowrite.readlines()
            # remove header
            header = members[0]
            members.pop(0)

            inactives = [member for member in members if ("no" in member)]

            filetowrite.seek(0)
            filetowrite.write(header)
            for member in members:
                if member in inactives:
                    filetoappend.write(member)
                else:
                    filetowrite.write(member)
            filetowrite.truncate()


memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)


headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())
