user= ['Dave', 'John', 'Ram']
ab=['Dave', 42, True]
emptylist=[]
print("Dave" in user)
#True
print("Dave" in emptylist)
#False
user+=['Shaym']
print(user)
#['Dave', 'John', 'Ram', 'Shaym']
#  user+='Shaym'
print(user)
#['Dave', 'John', 'Ram', 'Shaym', 'S', 'h', 'a', 'y', 'm']
#notice how by not enclosing it in square brackets we get each charachter of shyam in the list
#  user.append('Riya')
print(user)
#TypeError: list.append() takes exactly one argument (2 given)
#so we can only use append for just one argument
user.extend(['Riya','Priya'])
print(user)
#['Dave', 'John', 'Ram', 'Shaym', 'Riya', 'Priya']

print(user[2]) #Ram The indexing starts with 0
print(user[2:4]) #['Ram', 'Shaym']
print(user[2:-1])#['Ram', 'Shaym', 'Riya']
#So while using ':' here, the starting index is included while the last one is not included unlike string

user.insert(0,'Kanha')
print(user) #['Kanha', 'Dave', 'John', 'Ram', 'Shaym', 'Riya', 'Priya']
#added at index 0
user[2:2]=['Keshav','Rythem']
print(user) #['Kanha', 'Dave', 'Keshav', 'Rythem', 'John', 'Ram', 'Shaym', 'Riya', 'Priya']
#added them at index 2 without changing the list because the starting and ending index is same
user[1:3]=['Divyansh','Shubh']
print(user) #['Kanha', 'Divyansh', 'Shubh', 'Rythem', 'John', 'Ram', 'Shaym', 'Riya', 'Priya']
#changed at index 1 and went on till less than 3(because remember it does not include the last index here)
user.remove('Kanha')
print(user)#['Divyansh', 'Shubh', 'Rythem', 'John', 'Ram', 'Shaym', 'Riya', 'Priya'] 
#can be used to remove any element from the list
print(user.pop()) #Priya
print(user)#['Divyansh', 'Shubh', 'Rythem', 'John', 'Ram', 'Shaym', 'Riya']
#REMOVE LAST ELEMENT AND PRINT
# user.clear()
# print(user) #[]
#clear erases all data from the list
# del user
# print(user)
#NameError: name 'user' is not defined. as the list itself has been erased.
user.sort()
print(user) #['Divyansh', 'John', 'Ram', 'Riya', 'Rythem', 'Shaym', 'Shubh']
nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)#[5, 1, 78, 42, 4]
#simply reverse the list
# nums.sort(reverse=True)
# print(nums) #[78, 42, 5, 4, 1]
#descending order
#Remeber that sort modifies the original list
#but if we want it to not change we can use sorted
print(sorted(nums,reverse=True)) #[78, 42, 5, 4, 1]
print(nums) #[5, 1, 78, 42, 4] we commented out the previous nums.sort so the original list was [5, 1, 78, 42, 4]
#There are 3 ways to copy a list
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(numscopy)#[5, 1, 78, 42, 4]
print(mynums)#[5, 1, 78, 42, 4]
print(mycopy)#[5, 1, 78, 42, 4]
mycopy.sort()
print(mycopy)#[1, 4, 5, 42, 78]
print(nums)#[5, 1, 78, 42, 4]
print(type(nums)) #<class 'list'>


#TUPLES

#tuples are lists which cannot be changed i.e we cannot change the values of a tuple