import os
import json

class System_init:
    @staticmethod
    def FileCreation():
        files = ["data.json","players.json","matches.json","teams.json","playerStats.json","updates.json","season.json"]
        for i in files:
            if not os.path.isfile(i):
                with open(i,"w+") as fp:
                    json.dump({},fp)
    def PlayerFile(PlayerFileName = "players.json"):
        with open(PlayerFileName,"w") as fp:
            json.dump({},fp)

    def TeamFile(TeamFileName ="teams.json" ):
        with open(PlayerFileName,"w") as fp:
                json.dump({},fp)
    def MatchFile(MatchFileName = "matches.json",TeamFileName = "teams.json" ):
        for i in teams:
            data[i] = {}
        with open(MatchFileName,"w") as fp:
            json.dump(data,fp)

