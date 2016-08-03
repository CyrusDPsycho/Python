
def Steps(x,y):
    bot_steps = [a-b for a,b in zip(x,y)]
    return bot_steps

m = input()
bot_stepcount = 0

'''
#Print the input Grid

print "GRID"
'''

grid = []
for i in xrange(0, int(m)):
    grid.append(raw_input().strip())

'''
#Printing the grid line by line
for j in grid: 
    print j
'''    

    
for botr in range(0, len(grid)):
    for botc in range(0, len(grid[botr])):
        if(grid[botr][botc] == 'm'):
            bot_loc = [botr,botc]
            
        if(grid[botr][botc] == 'p'):
            pr_loc = [botr,botc]
'''   
#Printing the location of the bot and the princess

print "\nLOCATION"           
print "Bot", bot_loc
print "Princess", pr_loc
print "  " 
'''
bot_steps = [pr_loc,bot_loc]

while(bot_steps!=[0,0]):
    bot_steps = Steps(pr_loc,bot_loc)
#    print "\nBot Steps\n", bot_steps , "\n"  #Printing the bot steps 
    
        
    bot_stepcount+=1
#    print 'Bot Step Count', bot_stepcount #Printing the no: of steps the bot
                                           #takes to reach the princess    
    Steps(pr_loc,bot_loc)
    
    if(bot_steps[0]>0):
        bot_loc[0]+=1
        print "DOWN"
    elif(bot_steps[0]<0):
        bot_loc[0]-=1
        print "UP"
    elif(bot_steps[1]>0):
        bot_loc[1]+=1
        print "RIGHT"
    elif(bot_steps[1]<0):
        bot_loc[1]-=1
        print "LEFT"

    
#print "\nFinal Bot Position", bot_loc  #Print the final location of the bot
