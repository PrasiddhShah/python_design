class Journal:
    def __init__(self):
        self.entries=[]
        self.count =0
    def add_entry(self,text):
        self.count +=1
        self.entries.append(f"{self.count}: {text}")
    def remove_entry(self, pos):
        del self.entires[pos]
        if self.count >0:
            self.count -=1
    def __str__(self):
        return '\n'.join(self.entries)
    
    # This is a no no, we might have to change this down the line
    # and if we have saves like this in multiple class we will have to go and change
    # all the different "save/load" in all the places THIS IS NOT GOOD!!!
    
    
    # def save(self,filename):
    #     file = open(filename,"w")
    #     file.write()
    #     file.close()
    
    # def load(self,filename):
    #     pass
    # def load_from_web(self, uri):
    #     pass

class PersistenceManager:
    @staticmethod
    def save_to_file(journal,filename):
        file = open(filename,'w')
        file.write(str(journal))
        file.close()



if __name__ == "__main__":
    j = Journal()
    j.add_entry("I join google today.")
    j.add_entry("I liked it so much.")
    print(f"Journal entire:\n{j}")

    file = r'journal.txt'
    PersistenceManager.save_to_file(j,file)

    with open(file) as f:
        print(f.read())
        f.close()