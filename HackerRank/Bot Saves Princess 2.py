#!/bin/python

#Function to calculate the no: of steps away from the princess
def Steps(botx,boty,prx,pry):
    return(prx-botx,pry-boty)

n = int(raw_input().strip())
bot_loc = list(map(int,raw_input().split()))

#GRID 
grid = []
for i in xrange(n):
    grid.append(raw_input().strip())
    
#for j in grid:
#    print j           #Print Grid
    
    
#Princess Location And Bot Location
'''
for botr in xrange(n):
    for botc in xrange(n):
        if grid[botr][botc] == 'p':
            pr_loc = [botr,botc]
'''          
        
pr_loc = [[botr,botc] for botc in xrange(n) for botr in xrange(n) if grid[botr][botc] == 'p']

#print "\nPrincess Location ",pr_loc
#print "\nBot Location ",bot_loc


#To find which direction to move in

bot_steps = Steps(bot_loc[0],bot_loc[1],pr_loc[0][0],pr_loc[0][1])
#print "\n Bot Steps", bot_steps

if(bot_steps[1]<0):
    print "LEFT"
elif(bot_steps[1]>0):
    print "RIGHT"
elif(bot_steps[0]>0):
    print "DOWN"
elif(bot_steps[0]<0):
    print "UP"
    
