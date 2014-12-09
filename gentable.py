from string import Template

class player:
    def __init__(self, name='[Player]'):
        """ Creates a dictionary with fields for the stats of a single Player."""
        self.stats = {}
        self.AddField('Games', 0)
        self.AddField('Wins', 0)
        self.AddField('Losses', 0)
        self.AddField('Points', 0)
        self.AddField('Name', name)
    
    def GetValue(self, field):
        return self.stats[field]
    
    def AddField(self, field, value):
        self.stats[field] = value
        
    def WinLoss(self, value):
        """ If value is 1, it counts as a win, if value is 0 game is a loss"""
        if value == 1:
            self.stats['Wins']+=1
        else:
            self.stats['Losses']+=1
        
        self.stats['Games']+=1
    
    def AddPoints(self, points):
        self.stats['Points']+=points
        
    def MakeStats(self):
        g = self.GetValue('Games')
        w = self.GetValue('Wins')
        l = g-w
        wp = 100.0*w/g
        p = self.GetValue('Points')
        ppg = 10.0*p/g
        f_ppg = int(ppg % 10)
        i_ppg = int(ppg /10.0)
        self.AddField('WP',str(int(wp))+'%')
        self.AddField('PpG',str(i_ppg)+'.'+str(f_ppg)) 
        
    def DispStats(self):
        if 'PpG' not in self.stats:
            self.MakeStats()
            
        print "Player: " + self.GetValue('Name')
        print "Win Percentage: " + self.GetValue('WP')
        print "Wins/Losses: " + str(self.GetValue('Wins')) + "/" + str(self.GetValue('Losses'))
        print "Total Points Scored/Points per Game: " + str(self.GetValue('Points')) + ' / ' + self.GetValue('PpG')
    
class match:
    """Holds the data corresponding to a single game of foosball."""
    def __init__(self):
        self.data = {}
      
    def AddField(self, field, value):
        self.data[field] = value
      
    def GetValue(self, field):
        return self.data[field]
      
    def DispData(self):
        for field in self.data:
            print (field, self.data[field])

    def Data2Table(self, rownum=1):
        code = '''<tr class="row$num">
    <td>$DATE</td>
    <td>$RED</td>
    <td>$WHITE</td>
    <td>$SCORE</td>
</tr>'''
        html_table = Template(code)
        return html_table.substitute(num=rownum, DATE=self.GetValue('DATE'), RED=self.GetValue('RDTM'), WHITE=self.GetValue('WHTM'), SCORE=self.GetValue('FSCR'))
        
    def GetField(self, value):
        """Searches the fields of a match to find value. It returns the field that contains it"""
        f = ""
        for field in self.data:
            if value==self.GetValue(field):
                f = field
        return f

    def MakeTeams(self):
        """This function reads the values loaded into a match object and puts the teams in a form to be written as text. It expects fields RPL1, RPL2, WPL1 and WPL2, which are the first and second players on the red and white teams respectively. It will add fields, RDTM, and WHTM, which have the text formatted team strings."""
        wt = ''
        rt = ''
        r = []; # List of red team members
        w = []; # List of white team members
        for num in range(1,3):
            r.append(self.GetValue('RPL'+str(num)))
            w.append(self.GetValue('WPL'+str(num)))
         
        if len(r[1])==0 or r[0]==r[1]:
            rt = r[0]
        else:
            rt = r[0]+"/"+r[1]
            
        if len(w[1])==0 or w[0]==w[1]:
            wt = w[0]
        else:
            wt = w[0]+"/"+w[1]
         
        self.AddField('RDTM', rt)
        self.AddField('WHTM', wt)

    def MakeFinalScore(self):
        """This function takes the points that each team scored, RDSC, WHSC and adds a field for the final score FSCR. Also defines a token for WNNR, being 1 if the red team won and 2 if the white team won"""
        rd = str(self.GetValue('RDSC'))
        wh = str(self.GetValue('WHSC'))
        win_val = (int(rd)<int(wh)) + 1
        win = ''
        if win_val==1:
            win = 'R'
        else:
            win = 'W'
        self.AddField('FSCR', rd + ' - ' + wh)
        self.AddField('WNNR', win)

def File2Dict(filename):
    fid = open(filename)
    matches = [] # List for matches
    while 1:
        line = fid.readline()
        if not line:
            break
        field = line[:4]
        if field=='####':
            tempmatch=match()
            matches.append(tempmatch) # Make new match
        else:
            value = line[5:]
            if value[-1:]=='\n':
                value = line[5:-1]
            matches[-1].AddField(field, value) # Add data to last match
    
    fid.close()
    
    for m in matches:
        #Add in the final scores and teams
        m.MakeTeams()
        m.MakeFinalScore()
        
    return matches

def writeHTMLtableMatches(match_list, player_list, fileout='foosball.html', max_matches=999):
    """This function writes HTML code to a file"""
    data = []
    i = 0
    table = ''
    
    # Load in the header file
    in_file = open('f_head.txt')
    data.append(in_file.read())
    in_file.close()
    
    fid = open('f_mid.txt')
    player_stats = Template(fid.read())
    fid.close()
    
    #sub_list = dict([
        
    
    mid = player_stats.substitute(ZCWins=player_list['Z. Conway'].GetValue('Wins'), ZCPer=player_list['Z. Conway'].GetValue('WP'), ZCPoints=player_list['Z. Conway'].GetValue('Points'), MLWins=player_list['M. Liepe'].GetValue('Wins'), MLPer=player_list['M. Liepe'].GetValue('WP'), MLPoints=player_list['M. Liepe'].GetValue('Points'), SPWins=player_list['S. Posen'].GetValue('Wins'), SPPer=player_list['S. Posen'].GetValue('WP'), SPPoints=player_list['S. Posen'].GetValue('Points'), NVWins=player_list['N. Valles'].GetValue('Wins'), NVPer=player_list['N. Valles'].GetValue('WP'), NVPoints=player_list['N. Valles'].GetValue('Points'), YXWins=player_list['Y. Xie'].GetValue('Wins'), YXPer=player_list['Y. Xie'].GetValue('WP'), YXPoints=player_list['Y. Xie'].GetValue('Points'))
    
    data.append(mid)
    
    for match in match_list:
        curMatchHTML = match.Data2Table((i % 2) + 1)
        data.append(curMatchHTML)
        table = table + curMatchHTML
        i+=1
        if i==max_matches:
            break
    
    # Load in the footer file
    in_file = open('f_foot.txt')
    data.append(in_file.read())
    in_file.close()
    
    # Write the text file
    out_file = open(fileout,'w')
    out_file.write(''.join(data))
    out_file.close()
    return data

def get_stats(match_list):
    """ This script searches the list matches and makes a dictionary containing a player class for each foosballer. It then stores their statistics for later reporting."""
    players = {}
    player_fields = ['WPL1', 'WPL2', 'RPL1', 'RPL2']
    t_abbr = dict([('W', 'WHSC'), ('R', 'RDSC')])

    for match in match_list:
        for player_position in player_fields:
            wl = 0;
            player_name = match.GetValue(player_position)
            t = t_abbr[player_position[0]]
            
            # If a player isn't in the player array, instantiate it.
            if player_name not in players:
                players[player_name] = player(player_name)
            
            #print player_name
            points = int(match.GetValue(t))/2.0
            
            # Tally the points they have accrued
            players[player_name].AddPoints(points)
            
            if match.GetValue('WNNR')==player_position[0]:
                wl = 1
                
            if player_position=='WPL2' or player_position=='RPL2':
                if player_position=='WPL2' and match.GetValue('WPL1')!=match.GetValue('WPL2'):
                    players[player_name].WinLoss(wl)
                if player_position=='RPL2' and match.GetValue('RPL1')!=match.GetValue('RPL2'):
                    players[player_name].WinLoss(wl)
            else:
                players[player_name].WinLoss(wl)
    
    for p in players:
        players[p].MakeStats()
            
    return players

# This section actually runs the script when the program is loaded
match_history = File2Dict('score.txt')
players = get_stats(match_history)

writeHTMLtableMatches(match_history, players)
