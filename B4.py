v = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
current_streak = 0
best_streak = 0
best_lenght = 1
current_lenght = 1

for i in range(1, len(v)):
    if v[i] < v[i - 1]: #Checks if the current reading dropped compared to the previous one
        current_lenght += 1 #increases current drop streak length
    else:
        current_lenght = 1 #resets streak lenght if drop seq break
        current_streak = i
        
    # Check for the record AFTER updating the length
    if current_lenght > best_lenght:
        best_lenght = current_lenght
        best_streak = current_streak

if current_lenght > best_lenght:
    best_lenght = current_lenght
    best_streak = current_streak

e = best_streak + best_lenght - 1 #calculates ending index of the longest streak

print("print('Longest continius drop:', best_lenght, 'mins')") # keeping your print text style
print("Started at:", v[best_streak], "v")
print("Ended at:", v[e], "v")
