class Labirynt:
    start = ();
    
    def __init__(self):
        with open('/home/student/labirynt0.txt') as f:
            self.lines = f.readlines()
        
    def findstart(self):
        x = self.lines[0]
        wys = ''
        szer = ''
        bl = True
        for i in range(len(x)):
            if x[i] <> ' ' and bl == True:
                wys = wys + x[i]
            if x[i] == ' ' and bl == True:
                bl = False
            if x[i] <> ' ' and bl == False:
                szer = szer + x[i]

        wys = int(wys)
        szer = int(szer)
        #print wys, szer

        for i in range(1,wys-1):
            for j in range(szer-1):
                if self.lines[i][j] == '@':
                    poczatek = [i,j]
        self.start = poczatek
        return poczatek
    
    def findend(self, cord = [] ):
        if self.lines[cord[0]][cord[1]] == '$':
            return True
        print self.lines[cord[0]][cord[1]]
        
        if self.lines[cord[0]+1][cord[1]] == ' ':
            self.findend([cord[0]+1, cord[1]])
        elif self.lines[cord[0]+1][cord[1]] == '#':
            return
            
        if self.lines[cord[0]-1][cord[1]] == ' ':
            self.findend([cord[0]-1, cord[1]])
            
        if self.lines[cord[0]][cord[1]+1] == ' ':
            self.findend([cord[0], (cord[1]+1)])
            
        if self.lines[cord[0]][cord[1]-1] == ' ':
            self.findend([cord[0], (cord[1]-1)])
            

            

Lab = Labirynt()
StartCords = Lab.findstart()
print StartCords
Lab.findend(StartCords)      
