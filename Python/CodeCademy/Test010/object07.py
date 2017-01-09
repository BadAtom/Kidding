import random

a = ["artless", "bawdy", "beslubbering", "bootless", "churlish", "cockered", "clouted", "craven", "currish", "dankish",
     "dissembling", "droning", "errant", "fawning", "fobbing", "froward", "frothy", "gleeking", "goatish", "gorbellied",
     "impertinent", "infectious", "jarring", "loggerheaded", "lumpish", "mammering", "mangled", "mewling", "paunchy",
     "pribbling", "puking", "puny", "qualling", "rank", "reeky", "rougish", "ruttish", "saucy", "spleeny", "spongy",
     "surly", "tottering", "unmuzzled", "vain", "venomed", "villanious", "warped", "wayward", "weedy", "yeasty"]

b = ["base-court", "bat-fowling", "beef-witted", "beetle-headed", "boil-brained", "clapper-clawed", "clay-brained",
     "common-kissing", "crook-pated", "dismal-dreaming", "dizzy-eyed", "doghearted", "dread-bolted", "earth-vexing",
     "elf-skinned", "fat-kidneyed", "fen-sucked", "flap-mouthed", "fly-bitten", "folly-fallen", "fool-born",
     "full-gorged", "guts-griping", "half-faced", "hasty-witted", "hedge-born", "hell-hated", "idle-headed",
     "ill-breeding", "ill-nurtured", "knotty-pated", "milk-livered", "motley-minded", "onion-eyed", "plume-puckered",
     "pottle-deep", "pox-marked", "reeling-ripe", "rough-hewn", "rude-growing", "rump-fed", "shard-borne",
     "sheep-biting", "spur-galled", "swag-bellied", "tardy-gaited", "tickle-brained", "toad-spotted", "unchin-snouted",
     "weather-bitten"]

c = ["apple-john", "baggage", "barnacle", "bladder", "boar-pig", "bugbear", "bum-bailey", "cancker-blossom",
     "clack-dish", "clotpole", "coxcomb", "codpiece", "death-token", "dewberry", "flap-dragon", "flax-wench",
     "flirt-gill", "foot-licker", "fustilarian", "giglet", "gudgeon", "haggard", "harpy", "hedge-pig", "horn-beast",
     "hugger-mugger", "joithead", "lewster", "lout", "maggot-pie", "malt-worm", "mammet", "measle", "minnow",
     "miscreant", "moldwarp", "mumble-news", "nut-hook", "pigeon-egg", "pignut", "puttock", "pumpion", "ratsbane",
     "scut", "skainsmate", "strumpet", "varlot", "vassal", "whey-face", "wagtail"]

amount = int(input("Amount of insults: "))

for i in range(0, amount):
    achoice = a[random.randint(0, len(a) - 1)]
    bchoice = b[random.randint(0, len(b) - 1)]
    cchoice = c[random.randint(0, len(c) - 1)]
    print(str(i + 1) + ".  Thou " + achoice, bchoice, cchoice + "!")