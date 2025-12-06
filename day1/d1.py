a = open('/home/alok/my_files/DSA/adventofcode/day1/d1_input.txt')

data = a.readlines() # [ 'R23', 'L10'.... ] L -> decrease; R-> increase

password = 0
dial = 50 # initial position is 50 [range is [0,99]  ]
print(f'initial dial is {dial}')
for line in data:
    dir = line[0] # R or L
    mag = int(line[1:len(line)]) # int magnitude
    

    # ----underflow----
    # if dial = n , we get Lm where m > n therefore n-m = negetive hence we can do this .. if m>n then {dial = dial+100 - m }
    # --------overflow-------
    # if dial = n , we get Rn such that n+m > 99 then we will {dial = (dial+m)%100}

    nmag = mag%100 # 28 of 528
    odial = dial # original Dial value before changing in this iteration
    if dir == 'L':
        if nmag>dial:
            dial += 100
        dial -= nmag

        print(f'turned left by {mag} dial is {dial}')
    elif dir == 'R':
        dial = (dial + mag)%100
        print(f'turned Right by {mag} dial is {dial}')
    
    hunds = int(mag/100) # no of hundreds in the mag
    password+=hunds # each hundred cause 1 tick to 0
    if( (mag%100!=0) and (dial ==0 or (dir =='L' and odial!=0 and (odial<dial)) or (dir =='R' and (dial < nmag+odial)))) :
        password+=1 # if anything in once or tense place  causes the dial to go to 0
        print(f'incrementing pass at {dir} , {mag}  pswd becomes {password}')
    
    
    
print(f'final dial is {dial}')
print(f'final password is {password}')
