class hardcodedinfo:
    roles = ["tank", "alac", "heal", "banner", "quick", "push"]
    affinity = ["none", "low", "med", "high"]
    role_amount_req = [1, 2, 2, 1, 2, 1]
    raiders = ["blue", "xun", "rexa", "lilo", "mela", "succ", "tini", "loki", "ninia"]
    toons = [["blue", ["alac", "hfb", "qfb"]], ["xun", ["alac", "pBoon"]],
             ["rexa", ["druid", "sqrapper"]], ["lilo", ["hfb", "alac"]],
             ["mela", ["sqrapper", "alac", "bs"]], ["succ", ["bs"]],
             ["tini", ["hfb", "qfb", "bs"]], ["loki", ["pBoon", "hfb"]],
             ["ninia", ["druid", "pBoon", "healren"]]]
    task_capacity = [[10, 10, 0, 0, 0, 0, 0],  # alac
                     [10, 0, 0, 10, 0, 5, 0],  # hfb
                     [10, 0, 0, 0, 0, 5, 0],  # qfb
                     [10, 10, 0, 0, 0, 0, 0],  # alac
                     [10, 0, 0, 0, 0, 5, 10],  # pBoon
                     [10, 0, 10, 0, 0, 0, 10],  # druid
                     [10, 0, 0, 0, 0, 5, 0],  # sqrapper
                     [10, 0, 0, 10, 0, 5, 0],  # hfb
                     [0, 10, 0, 0, 0, 0, 0],  # alac
                     [10, 0, 0, 0, 0, 5, 0],  # sqrapper
                     [10, 10, 0, 0, 0, 0, 0],  # alac
                     [0, 0, 0, 0, 10, 0, 0],  # bs
                     [0, 0, 0, 0, 10, 0, 0],  # bs
                     [10, 0, 0, 10, 0, 5, 10],  # hfb
                     [0, 0, 0, 0, 0, 5, 0],  # qfb
                     [0, 0, 0, 0, 10, 0, 0],  # bs
                     [10, 0, 0, 0, 0, 5, 10],  # pBoon
                     [10, 0, 0, 10, 0, 5, 0],  # hfb
                     [10, 0, 10, 0, 0, 0, 10],  # druid
                     [10, 0, 0, 0, 0, 5, 10],  # pBoon
                     [10, 10, 0, 10, 0, 0, 0]]  # healren

    task_affinity = [[3, 3, 0, 0, 0, 0],  # alac
                     [3, 0, 3, 0, 3, 0],  # hfb
                     [3, 0, 0, 0, 3, 0],  # qfb
                     [3, 3, 0, 0, 0, 0],  # alac
                     [3, 0, 0, 0, 2, 1],  # pBoon
                     [3, 0, 3, 0, 0, 3],  # druid
                     [2, 0, 0, 0, 2, 0],  # sqrapper
                     [1, 0, 2, 0, 3, 0],  # hfb
                     [0, 2, 0, 0, 0, 0],  # alac
                     [1, 0, 0, 0, 2, 0],  # sqrapper
                     [1, 3, 0, 0, 0, 0],  # alac
                     [0, 0, 0, 1, 0, 0],  # bs
                     [0, 0, 0, 3, 0, 0],  # bs
                     [3, 0, 3, 0, 3, 1],  # hfb
                     [0, 0, 0, 0, 3, 0],  # qfb
                     [0, 0, 0, 2, 0, 0],  # bs
                     [3, 0, 0, 0, 2, 1],  # pBoon
                     [3, 0, 3, 0, 3, 0],  # hfb
                     [3, 0, 3, 0, 0, 3],  # druid
                     [3, 0, 0, 0, 2, 1],  # pBoon
                     [3, 3, 2, 0, 0, 0]]  # healren
