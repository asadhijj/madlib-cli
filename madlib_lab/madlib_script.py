import re

print('''
        * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * 
        ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **  
        ** Hello Kidos, this is a game where you have to enter some words to define how a  **
        ** story goes using your own words, so please choose your words carefully, and     **
        ** unleash the power of your imagination!!                                         **
        ** * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * **
        * * * * * * * * * * * * * * * * * *  * * * * * * * * * * * * * * * * * * * * * * * * 
          ''')

def read_template(files):
    '''this function reads the file 
        using the path provided and
        returns its content if it exists
        otherwise it raises and error
     '''
    try:
        with open (files,"r")as file:
            return file.read()
    except:
        raise FileNotFoundError    


   
def parse_template(content):
    '''this function takes the file content and 
    removes the parts inside of curly brackets
    then return them in a tuple
    '''
    parts  = re.findall('{(.*?)}', content)
    filterd = re.sub('{.+?}', '{}', content)  
    return filterd,(tuple)(parts)  


def merge (fill_content,parts:tuple):
    '''this function merges the game template with the user input and returns
    the template filled with the input
    '''
    return fill_content.format(*parts)
  
   
def gamefun():
    '''
    this function returns the whole game script with the added parts from the user and prints it,
    it also writes the in a new text file
    '''
    
    our_game_text = read_template("assets/make_me_a_video_game_template.txt")
    filterd , parts = parse_template(our_game_text)
    print(parts)
    values = list()
    for part in parts:
        values.append(input(f"\n please enter a {part}\n"))
    with open("make_me_a_video_game_template_result.txt",'w') as file:
        game = merge(filterd,(tuple)(values))
        file.write(game)
        print(game)
                        
                
        
    
       
if __name__ =="__main__":
      gamefun()   
