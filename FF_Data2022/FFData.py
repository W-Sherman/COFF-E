import re
import numpy as np
import matplotlib.pyplot
import itertools
import pandas as pd
from tqdm import tqdm
from strsimpy.jaccard import Jaccard

def get_name(in_name):
    name = re.sub("[\(\[].*?[\)\]]", "",in_name)
    if " " in name:
        name = name.split()
    if "-" in name[0]:
        name = name[0].split("-")
        outname = name
    else:
        outname = name

    return outname

def similar(a, b):
    jaccard = Jaccard(1)
    return jaccard.similarity(a,b)

def pull_database(url):
    
    dfs = pd.read_html(url)
    data = dfs[0]

    return data

def save_data_to_csv(df,path):
    with open(path+'nanosatsDatabase_Data.csv','w') as csv_file:
        df.to_csv(path_or_buf=csv_file)

    print("CODE: Data saved.")

def import_data(csv):
    return pd.read_csv(csv)

def updateImport(path):
    url = "https://www.nanosats.eu/database"    #main database website
    data = pull_database(url)
    save_data_to_csv(data,path)

def collectData(hitsfile,databasefile):
    #import both the hits we found as well as the entire dataset
    hits = pd.read_csv(hitsfile)
    database = pd.read_csv(databasefile)

    #define out frame for output
    outMissions = pd.DataFrame(columns= ["Mission",'Organisation','Num Sats','Size/Mass','Homogenaity','Sub-Class','Launch','Status','Ref Index'])

    missionList = hits.Mission.unique()
    #print(missionList)
    for name in tqdm(missionList):
        if outMissions['Mission'].eq(name).any() == False:
            #outMissions.loc[len(outMissions.index)] = [name,
            #                                            hits['Mission'].value_counts.name,
            #                                            ]
            #print(name," | ",hits['Mission'].value_counts()[name]," | ",database['Organization'][])

            hit = hits.loc[hits['Mission']==name].iloc[0]['i']

            hitfull = hits.loc[hits['Mission']==name].index
            
            count = hits['Mission'].value_counts()[name]

            org = database.iloc[hit]['Organisation']

            sm = database.iloc[hit]['Type (U/mass)']

            if database.loc[hitfull]['Type (U/mass)'].nunique() == 1:
                homo = 'identical'
            else:
                homo = 'different'

            if 'formation' in database.iloc[hit]['Mission description']:
                arch = 'formation'
            elif 'constellation' in database.iloc[hit]['Mission description']:
                arch = 'constellation'
            else:
                arch = 'idk'

            laun = database.iloc[hit]['Launch date']

            stat = database.iloc[hit]['Status']

            outMissions.loc[len(outMissions.index)] = [name,org,count,sm,homo,arch,laun,stat,hit]

    return outMissions

def findMVM(file,num=None,export=False):
    data_in = import_data(file)
    # Need to filter data to only include mission that may be multi-vehice flight mission'

    """s
    formations = data['Mission description'].str.contains('formation',case=False)
    print(formations)
    """
    hitMissions = pd.DataFrame(columns= ["Mission",'Sat Name','i','j'])

    if num:
        testset = data_in[0:num] #testdata
    else:
        testset = data_in
    numsats = len(testset)
    combs = list(itertools.combinations(list(range(numsats)),2))


    testset["Mission name"] = testset['Mission name'].str.replace(r"\s*\([^()]*\)", "", regex=True).str.strip()

    """formations = testset['Mission description'].str.contains('formation',case=False).sum()
    constellations = testset['Mission description'].str.contains('constellation',case=False).sum()
    swarms = testset['Mission description'].str.contains('swarm',case=False).sum()
    print(formations, constellations, swarms)"""

    for index in tqdm(combs):
        i = index[0]
        j = index[1]
        #print(i,j, end='\r')
        if i == j:
            continue
        elif testset['Launch date'][i] != testset['Launch date'][j]:
            continue
        elif testset['Organisation'][i] != testset['Organisation'][j]:
            continue
        elif testset['Mission description'][i] != testset['Mission description'][j]:
            continue
        elif similar(testset['Mission name'][i],testset['Mission name'][j]) <= 0.5:
            continue
        splitname_i = testset['Mission name'][i].replace("-"," ")
        splitname_i = splitname_i.split()
        #numsats_list.append(splitname_i[0])
        #if splitname_i[0] == 'PEARLS':
        #    print(testset['Mission name'][i],testset['Mission name'][j], similar(testset['Mission name'][i],testset['Mission name'][j]), i, j)
        
        if hitMissions['Sat Name'].eq(testset['Mission name'][i]).any() == False:
            hitMissions.loc[len(hitMissions.index)] = [splitname_i[0],
                                                        testset["Mission name"][i],
                                                        i,
                                                        j]
        if hitMissions['Sat Name'].eq(testset['Mission name'][j]).any() == False:
            hitMissions.loc[len(hitMissions.index)] = [splitname_i[0],
                                                        testset["Mission name"][j],
                                                        i,
                                                        j]
        """if hitMissions['Sat Name'].eq(testset['Mission name'][j]).any() == False:
            hitMissions.loc[len(hitMissions.index)] = [splitname_i[0],
                                                        testset["Mission name"][j],
                                                        testset['Organisation'][j],
                                                        testset["Type (U/mass)"][j],
                                                        testset['Launch date'][j],
                                                        testset['Status'][j]]"""
                                                        
    if export:
        hitMissions.to_csv('MVMhitList.csv', header=True)
            
    return hitMissions


if __name__ == "__main__":
    path = '/Users/will/Desktop/EDUCATION/SSDL/2_Research/Formation Flight Optimization/'
    #updateImport(path)

    file = "nanosatsDatabase_Data.csv"
    hitfile = "MVMhitList.csv"

    hitMissions = findMVM(file,export=True)

    out = collectData(hitfile,file)
    out.to_csv('Collected_MVMdata.csv')

    #sat_count = hitMissions['Mission'].value_counts()
    #print(sat_count)
