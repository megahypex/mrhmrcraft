import commands

class data:
    def getData(self):
        commandData = {
            "status" : {
                "Info" : """
                Displays the status of the server (Online / Offline)
                """,
                "Run" : commands.status
            },

            "ip" : {
                "Info" : """
                Displays the latest IP Address of the server
                """,
                "Run" : commands.ip
            },

            "smphelp" : {
                "Info" : """
                Displays all commands with usage
                """,
                "Run" : commands.smphelp
            }
        }
        return commandData

    def getPrefix(self):
        return "-"