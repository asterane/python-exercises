from random import randint
done = False
first = True
print("Welcome to the Professor Noggin Game Die!")
while not done:
    if done != False: break
    if first == True: input('Press Enter to roll the die.\n')
    dino = randint(1,3)
    if dino == 1:
        print("Roll:    11")
        print("        111")
        print("      11111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("        111")
        print("      1111111")
        print("      1111111\n")
        
    if dino == 2:
        print("Roll:  22222222")
        print("     222222222222")
        print("   22222      22222")
        print("  22222        22222")
        print("  2222          2222")
        print("               2222")
        print("             2222")
        print("           2222")
        print("         2222")
        print("       2222")
        print("     2222")
        print("    2222")
        print("   2222")
        print("  222222222222222222")
        print("  222222222222222222\n")
        
    if dino == 3:
        print("Roll:  33333333")
        print("     333333333333")
        print("   33333      33333")
        print("  33333        33333")
        print("  3333          3333")
        print("               3333")
        print("             3333")
        print("           3333")
        print("             3333")
        print("               3333")
        print("  3333          3333")
        print("  33333        33333")
        print("   33333      33333")
        print("     333333333333")
        print("       33333333\n")
        
    end = input('Press Enter to roll (type "done" to end)\n')
    if end.lower().startswith('d'):
        done = True
    first = False
