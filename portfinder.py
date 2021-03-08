from mcstatus import MinecraftServer

serverIp = input("Enter IP without port: ")

# Pinging is your responsibility and takes time, pick your range accordingly.
# Default server port is 25565
startingPort = 25550
endingPort = 25580

print("Now testing ports", startingPort, "-", endingPort)
for i in range(startingPort, endingPort + 1):
    try:
        serverObject = MinecraftServer.lookup(serverIp + ":" + str(i))
        print(i, "-", serverObject.query().motd,
              "[", serverObject.status().players.online, "/", serverObject.status().players.max,
              "🔌", serverObject.status().version.protocol, "]")
    except:
        print(i, "- ❌")
