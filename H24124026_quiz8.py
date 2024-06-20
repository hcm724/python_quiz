import csv

def read_csv(filename):
	#打開要求檔案file name
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  				#跳過第一行標題
        data = [row for row in reader]
    return header, data

def calculate_win_percentage(record):		#進行勝率計算
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)

def task1(data):
    eastern_teams = [row for row in data if row[0] == 'Eastern']
    result = []								#建立空list將符合結果的隊伍放入list中
    for team in eastern_teams:
        home_win_pct = calculate_win_percentage(team[7])
        away_win_pct = calculate_win_percentage(team[8])
        if home_win_pct < away_win_pct:
            result.append(team[1])
    return result

def task2(data):
    eastern_teams = [row for row in data if row[0] == 'Eastern']
    western_teams = [row for row in data if row[0] == 'Western']

    #計算得分-失分的平均
    eastern_avg_pf_pa = sum(int(team[5]) - int(team[6]) for team in eastern_teams) / len(eastern_teams)
    western_avg_pf_pa = sum(int(team[5]) - int(team[6]) for team in western_teams) / len(western_teams)

    #回傳較高得分的結果
    return 'Eastern' if eastern_avg_pf_pa > western_avg_pf_pa else 'Western'

def task3(data):
	# 假設第11列是 InterConference_Wins
	# 第12列是 InterConference_Games
    for team in data:
        team.append(float(team[10]) / float(team[11]))  # 計算對另一聯盟的勝率
    sorted_teams = sorted(data, key=lambda x: x[-1], reverse=True)
    return [team[1] for team in sorted_teams]


# read data
header, nba_data = read_csv('pe8_data.csv')

# task1
task1_result = task1(nba_data)

# task2
task2_result = task2(nba_data)

# task3

task3_result = task3(nba_data)

# 输出结果
print("(1):")
print("\n(2):")
print(task2_result)
print("\n(3):")
print(task3_result)