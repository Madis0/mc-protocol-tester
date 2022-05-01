# This script requires mcstatus. See https://github.com/Dinnerbone/mcstatus or pip install mcstatus
from mcstatus import JavaServer

# Version numbers can be spoofed by server so it is better to check for protocol numbers instead
# 1.8.x is 47, others can be seen at https://wiki.vg/Protocol_version_numbers
startingProtocol = 47

# File to use for input. Needs to have a list of server IPs (with ports, if needed), one IP per row.
inputFile = "servers.txt"

# File to save the files in, if the user chooses so.
outputFile = "goodServers.txt"

# Store testable servers in an array
testableServers = []

# Store good servers in an array
goodServers = []

# Extract file inputFile to array testableServers
try:
    fileObject = open(inputFile, 'r')
    print("Loading servers to memory...")
    for row in fileObject:
        if "." in row:
            testableServers.append(row.strip())
        else:
            exit("This row has invalid data: " + row + "\nPlease fix it before running this script.")
    fileObject.close()
    print("Servers have been loaded, now checking the protocols...\n")
except IOError:
    print("Please create a file called " + inputFile + " that contains a list of server IPs, one IP per row.")

# Parse testableServers and place the good ones to goodServers
for server in testableServers:
    try:
        serverObject = JavaServer.lookup(server)
        serverStatus = serverObject.status()

        if serverStatus.version.protocol > startingProtocol:
            goodServers.append(server)
            print(server, "is using protocol", serverStatus.version.protocol,
                  "which claims to be", serverStatus.version.name)
    except OSError:
        print(server, "had an error, please check the IP and port.")
print("\nEnd of file. Any servers that did not appear here are not using protocol " + str(startingProtocol + 1)
      + " or higher.")

# Ask whether the user wants to save the output to the outputFile
outputServers = input("Type y(es) to output the good servers to file " + outputFile + ": ")
if outputServers == "y" or outputServers == "yes" or outputServers == "y(es)":
    try:
        fileObject = open(outputFile, 'a')
        print("Creating the file...")
        for server in goodServers:
            fileObject.write(server + "\n")

        fileObject.close()
        print("Good servers have successfully been written to the file.")
    except IOError:
        print("Could not create a file called " + outputFile + ", do you have the necessary permissions?")
