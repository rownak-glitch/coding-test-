import click 

courses= {'0':['English grammar','John Smith '], 
          '1': ['Mathematics','Lara Gilbert'],     # used dictionary data structure
          '2': ['Physics','Johanna Kabir'],
          '3': ['Chemistry','Daniel Robertson'],
          '4': ['Biology','Larry Copper']}

day=0
hour=0
co=0
routine ={co: [day,hour]}
@click.group()
def main():
    pass

@main.command()
def C():
    """List courses with teachers Name"""
   
    for sub, teac in courses.values():
             print(sub,',',teac)

@main.command()
def A():
    """Create Routine"""
    for sub,teac in courses.values():
        print(sub)
    global day
    global hour
    global co
    day= click.prompt("Enter Day")
    hour=click.prompt("Enter Hour")
    co=click.prompt("Enter course")
    day= '{}'. format(day)
    hour='{}'. format(hour)
    co='{}'. format(co)
    print(day)
    print(hour)
    print(co)
    
    
    
    

@main.command()       
def B():
    """ Show Routine"""  
    global routine
    routine ={co: [day,hour]}
    print (routine)

        
    









if __name__=='__main__':
     main()   