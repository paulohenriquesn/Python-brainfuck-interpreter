#PauloHenrique
pointerMemory = []
currentPointer = 0
codeBrainFuck = input("")
memory = [0,0,0,0,0]

def printLine():
    for i in range(24):
        print('[{}] - {}'.format(i,pointerMemory[i]))

for i in range(24):
    pointerMemory.append(0)

i = -1       
while i < len(codeBrainFuck)-1:
    i+=1
    if(memory[3] == 0):
        memory[0] = i
        memory[1] = currentPointer
        memory[2] = pointerMemory[currentPointer]
        memory[3] = 1
    print(codeBrainFuck[i])
    if(codeBrainFuck[i] == '+'):
        pointerMemory[currentPointer] +=1
    if(codeBrainFuck[i] == '-'):
        if(pointerMemory[currentPointer] > 0):
            pointerMemory[currentPointer] -=1
    if(codeBrainFuck[i] == '>'):
        currentPointer +=1
    if (codeBrainFuck[i] == '<'):
        currentPointer -=1
    if (codeBrainFuck[i] == '['):
        memory[0] = i
        Count = 1
        while(Count > 0):
            if(pointerMemory[currentPointer] > 0):
                i+=1
                Count = 0
            i-=1
    if (codeBrainFuck[i] == ']'):
        memory[4] = i
        if (pointerMemory[memory[1]] > 0):
            i = memory[0]
    if(codeBrainFuck[i] == '.'):
        print(chr(pointerMemory[currentPointer]))
    if (codeBrainFuck[i] == ','):
        ch = input('>')
        pointerMemory[currentPointer] = ord(ch)
            
                
    
   
                    
    
print(9*'-')
printLine()
        
