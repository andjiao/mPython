
#True/False skal starte med stort ellers godtaages den ikke
#boolean is short circuit which means 
# when python intrepreator wnats to evaulate an expression it starts from the the first argument
#if the first argument is true it continues to evaluaate to see if the second arguments is also true
#however as soon as an expression is false the evaluation stops
#fx. if high_income is false, the evaluater stops 
# and the rest will also will be false bc at leaast one of the arguments and one of the operands is false 
#so the evaluation stops as soon as one of the arguments evaluets to false 
high_income = False
good_credit = True
student = True

# with or arguments at leaast one of the arguments has to be true 
#so the evaluations stops as soon as we find an argument that evaluets to true 
#so of high_income is false, it continues to next, hoping that the next statements is true 
#so if good_credit is true, the evaluation stops and the whole expression will be true 
if(high_income or good_credit) and not student:
    print("eligable")
else:
    print("not eligable")