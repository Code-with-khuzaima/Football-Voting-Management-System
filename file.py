#Football Vote Managment System


class vote_managment_system():
    def __init__(self):
        self.total_vote=0
        self.cr=0
        self.messi=0
        self.neymar=0
        self.mbape=0
        self.haland=0
        self.user_list=[]
    


    def vote_managment(self):
        print('Welcome To Vote Result')
        print('1.Winner \n2.Ranking')
        sel_opt=int(input('Select Any option from above:'))
        if sel_opt==1:
               dict={
                   'goat':self.cr,
                   'short guy':self.messi,
                   'brazillian':self.neymar,
                   'black_guy':self.mbape,
                   'moster':self.haland
                   
               }
               winner=max(dict,key=dict.get)
               print(f'winner is {winner}')

        elif sel_opt==2:
          rank={
                   'goat':self.cr,
                   'short guy':self.messi,
                   'brazillian':self.neymar,
                   'black_guy':self.mbape,
                   'moster':self.haland
                   
               }
          ranking=sorted(rank.items(), key=lambda x:x[1], reverse=True)
          print('Ranking')
          for i, (name,score) in enumerate(ranking,start=1):
              print(f'{i}.{name}:{score}')
        else:
               print('Plz Select Corect Option')
            

        

    def user_managment(self):
        print('Welcome To User Managment Section')


        print('1.add User \n2.Delete User')
        sel_opt1=int(input('Select Option From above:'))


        if sel_opt1==1:
             inp_us=int(input('Enter user id:'))
             if inp_us in self.user_list:
              print('User already Exist')
             else:
              self.user_list.append(inp_us)
             print('user succefully added')
        elif sel_opt1==2:
             inp_us_del=int(input('Enter user id that u want to delete:'))
             if inp_us_del in self.user_list:
                 
              self.user_list.remove(inp_us_del)
              print('user succefully removed')
             else:
                 print('User Doesnt exist')
        else:
              print('Plz Enter Correct Option')

    def voting(self):
        print('welcome to voting center')
        user_id_input=int(input('Enter User id:'))
        if user_id_input in self.user_list:
            print('here are options \n1.Cristiano Ronaldo \n2.Messi \n3.Neymar \n4.mbappe \n5.halland')
            inp_vote=int(input('Enter Selected Option Here:'))
            if inp_vote==1:
                self.cr+=1
                self.total_vote+=1
                self.user_list.remove(user_id_input)
                print('Vote is succefully added')
            elif inp_vote==2:
                self.total_vote+=1
                self.messi+=1
                self.user_list.remove(user_id_input)
                print('Vote is succefully added')
            elif inp_vote==3:
                self.total_vote+=1
                self.neymar+=1
                self.user_list.remove(user_id_input)
                print('Vote is succefully added')
            elif inp_vote==4:
                self.total_vote+=1
                self.mbape+=1
                self.user_list.remove(user_id_input)
                print('Vote is succefully added')
            elif inp_vote==5:
                self.total_vote+=1
                self.haland+=1
                self.user_list.remove(user_id_input)
                print('Vote is succefully added')
            else:
                print('Plz Select Correct Option')
        else:
            print('User Id doesnt EXist')
            vote_managment_system.user_managment(self)
    def users(self):
        print(f'here are all users')
        for items in self.user_list:
            print(items)
    def exit(self):
        exit




def main():
    system=vote_managment_system()
    while True:
     
     print('WELCOME TO FOOTBALL VOTING CENTER')
     print("HERE IS OPTIONS SELECT ANY")
     print('1.Vote Result\n2.User Managment\n3.Voting POll\n4.ALL users\n5.exit')
     inp_vo=int(input('Enter Selected option here:'))
     if inp_vo==1:
         system.vote_managment()
     elif inp_vo==2:
         system.user_managment()
     elif inp_vo==3:
         system.voting()
     elif inp_vo==4:
         system.users()
     elif inp_vo==5:
         exit
         
     else:
         print('Plz Select Correct Option:')
main()
         
         