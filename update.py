def updateRecordInDB(collection, DETAILS):
  collection.update_one(
    {
      "_id" : {
        "rollNo" : DETAILS[0][0],
        "name" : DETAILS[0][1],
        "username" : DETAILS[0][2]
      }
    },
    {
      "$set": {
        "localRank" : int(DETAILS[1][0]),
        "globalRank" : int(DETAILS[1][0]),
        "branch" : DETAILS[2][0],
        "HR" : {
          "DS" : int(DETAILS[3][0]),
          "ALGO" : int(DETAILS[3][1]),
          "TOT" : int(DETAILS[3][2]),
        },
        "SI" : {
          "BASIC" : int(DETAILS[4][0]),
          "PRIMARY" : int(DETAILS[4][1])
        },
        "LC" : {
          "LCPS" : int(DETAILS[5][0]),
          "LCNC" : int(DETAILS[5][1]),
          "LCR" : int(DETAILS[5][2]),
          "TOT" : int(DETAILS[5][3])
        },
        "IB" : {
          "IBS" : int(DETAILS[6][0]),
          "TOT" : int(DETAILS[6][1])
        },
        "CC" : {
          "CCPS" : int(DETAILS[7][0]),
          "CCNC" : int(DETAILS[7][1]),
          "CCR" : int(DETAILS[7][2]),
          "TOT" : int(DETAILS[7][3])
        },
        "CF" : {
          "CFPS" : int(DETAILS[8][0]),
          "CFNC" : int(DETAILS[8][1]),
          "CFR" : int(DETAILS[8][2]),
          "TOT" : int(DETAILS[8][3])
        },
        "SPOJ" : {
          "SPS" : int(DETAILS[9][0]),
          "SP" : float(DETAILS[9][1]),
          "TOT" : int(DETAILS[9][2])
        },
        "IC" : {
          "IC1" : int(DETAILS[10][0]),
          "IC2" : int(DETAILS[10][1])
        },
        "TOTAL" : int(DETAILS[11][0])
      }
    }
  )
  print("Updated : " + DETAILS[0][0] + " " + DETAILS[1][0])

