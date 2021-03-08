from mcstatus import MinecraftServer

# Version numbers can be spoofed by server so it is better to check for protocol numbers instead
# 1.8.x is 47, others can be seen at https://wiki.vg/Protocol_version_numbers
startingProtocol = 47

serverIp = input("Enter version IP: ")
serverObject = MinecraftServer.lookup(serverIp).status()

print(serverIp, "uses protocol", serverObject.version.protocol, "which claims to be", serverObject.version.name)

if serverObject.version.protocol <= startingProtocol:
    print("❌ " + str(serverObject.version.protocol) + " is 1.8 or lower!")
else:
    print("✔ " + str(serverObject.version.protocol) + " is 1.9 or higher!")
