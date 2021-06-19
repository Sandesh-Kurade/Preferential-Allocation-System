# Preferential-Allocation-System

This can be used as a plugin to the Moodle.
currently working on that.
To use this the format of csv file must be same as given records2.csv file.
change sub names , min capping, max capping i.e. limit.

# Algorithm

 Step 1:START
 Step 2:read csv file.
 Step 3:input preference, subject, limit,data(name,cpi)
 Step 4:Sort the datavalues by CPI
 Step 5:Check preferences 
 Step 6:if the limit of subject is not exceeded go to step 7 else go to step 8
 Step 7:Allocate the subject as per the preference given
 Step 8: check for next preference & repeat the process from Step 6
 Step 9:else if the minimum count of the subject is not exceeded then discard the                          subject& check for the next preferences and allocate the subject
 Step 10:END.
