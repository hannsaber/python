#Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

students [0][1]='bryant'
print (students)
#In the sports_directory, change 'Messi' to 'Andres'
sports_directory ['soccer'][1]='Andres'
print (sports_directory)
#Change the value 20 in z to 30
z[0]['y']=30
print(z)

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(list):
    for i in range(0,len(list)-1):
        output=""
        for key,val in list[i].items():
            output+=f"{key} - {val},"
        print (output)


iterateDictionary(students) 
def iterateDictionary2(key_name,list):
    for i in range(0,len(list)):
        
        for key,val in list[i].items():
            if key_name == key:
                print (val)
            
iterateDictionary2('first_name',students)   
iterateDictionary2('last_name',students)    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printinfo(dict):
    for key,val in dict.items():
        print("=============================")
        print(f"{len(val)},{key.upper()}")
print(printinfo(dojo))
