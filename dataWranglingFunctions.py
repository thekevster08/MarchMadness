# function to, given a row, calculate what the difference between the two seeds was. 
def delta_seed(row):
    cond = (seeds['Season'] == row['Season'])
    return seeds[cond & (seeds['TeamID'] == row['Team1'])]['Seed'].iloc[0] - seeds[cond & (seeds['TeamID'] == row['Team2'])]['Seed'].iloc[0]

#Function to look up 
def delta_winPct(row):
    cond1 = (record['Season'] == row['Season']) & (record['WTeamID'] == row['Team1'])
    cond2 = (record['Season'] == row['Season']) & (record['WTeamID'] == row['Team2'])
    return (record[cond1]['wins']/record[cond1]['games']).mean() - (record[cond2]['wins']/record[cond2]['games']).mean()

def get_points_against(row):
    wcond = (dfW['Season'] == row['Season']) & (dfW['WTeamID'] == row['WTeamID']) 
    fld1 = 'LScore'
    lcond = (dfL['Season'] == row['Season']) & (dfL['LTeamID'] == row['WTeamID']) 
    fld2 = 'WScore'
    retVal = dfW[wcond][fld1].sum()
    if len(dfL[lcond][fld2]) > 0:
        retVal = retVal + dfL[lcond][fld2].sum() 
    return retVal

def get_points_for(row):
    wcond = (dfW['Season'] == row['Season']) & (dfW['WTeamID'] == row['WTeamID']) 
    fld1 = 'WScore'
    lcond = (dfL['Season'] == row['Season']) & (dfL['LTeamID'] == row['WTeamID']) 
    fld2 = 'LScore'
    retVal = dfW[wcond][fld1].sum()
    if len(dfL[lcond][fld2]) > 0:
        retVal = retVal + dfL[lcond][fld2].sum() 
    return retVal

def get_remaining_stats(row, field):
    wcond = (dfW['Season'] == row['Season']) & (dfW['WTeamID'] == row['WTeamID']) 
    fld1 = 'W' + field
    lcond = (dfL['Season'] == row['Season']) & (dfL['LTeamID'] == row['WTeamID']) 
    fld2 = 'L'+ field
    retVal = dfW[wcond][fld1].sum()
    if len(dfL[lcond][fld2]) > 0:
        retVal = retVal + dfL[lcond][fld2].sum()
    return retVal

def delta_stat(row, field):
    cond1 = (record['Season'] == row['Season']) & (record['WTeamID'] == row['Team1'])
    cond2 = (record['Season'] == row['Season']) & (record['WTeamID'] == row['Team2'])
    return (record[cond1][field]/record[cond1]['games']).mean() - (record[cond2][field]/record[cond2]['games']).mean()
  