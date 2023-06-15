def syllableCount(string):
    
    while True:
        good_action = False
        while not good_action:
            action = input("\n select an language:"
                           "\n enter 1 to select russian"
                           "\n enter 2 to exit"
                           "\n")
            if action.isdigit():
                action = int(action)
                if (1 <= action <= 3):
                    good_action = True
                else:
                    print("invalid input")
            else:
                print("invalid input")
                
        if action == 1:
            controlSyllable = set("яиоаыйуеэё")
            new_list = []   
            for word in string:
                count = 0
                for i in word:
                    if i in controlSyllable:
                        count += 1
                new_list.append(count)
            if len(new_list) == new_list.count(new_list[0]):
                print("Парам пам-пам")
            else:
                print("Пам парам")
        if action == 2:
            exit()
     
   