
import sys
import os
import time
startTime = time.time()


'''
    fxn :: inputHandler
        
    this function takes flags from the input
    and parses them to filter the files
    being search with the pathFinder
'''
def inputHandler():
    f = None
    s = None
    if (len(sys.argv) > 2):
        for arg in range(len(sys.argv)):
            if (sys.argv[arg] == '-f'):
                f = sys.argv[arg+1]
            elif (sys.argv[arg] == '-s'):
                s = sys.argv[arg+1]
                try:#exception where s (size) is NaN
                    s = int(s)
                except Exception as e:
                    print(e)
                    sys.exit(1)
    return f, s

'''
    class :: pathFinder

    recursively searches through a root directory
    and appends files found by flagged parameters
    to a resulting array
        
'''
class PathFinder():
    
    def __init__(self, path):
        self.path = path

    '''
        fxn :: search
            @param f :: fuzzy matching if a filename contains f it'll be appended
            @param s :: size matching if a file is greater than s it'll be appended

        recursively searches through a root directory
        and appends files found by flagged parameters
        to a resulting array
            
    '''
    def search(self,f=None,s=None):
        fn = []
        for dirpath, dirnames, files in os.walk(os.path.abspath(self.path)):
            
            if (f and s):
                for doc in files:
                    try: #exception on symbolically linked file.
                        stats = os.stat(dirpath + '/' + doc) #get file stats
                        stats = stats.st_size #get file size
                        if (stats > s and f in doc): #filter
                            fn.append(doc) #append
                    except Exception as e: #exeption on symbolically linked file
                        print(e) #print exception

            elif (f and not s):
                for doc in files:
                    if (f in doc):
                        fn.append(doc)

            elif (not f and s):
                for doc in files:
                    try:#exception on symbolically linked file
                        stats = os.stat(dirpath + '/' + doc)
                        stats = stats.st_size
                        if (stats > s):
                            fn.append(doc)
                    except Exception as e:
                        print(e)

            else:
                for doc in files:
                    fn.append(doc)

        return fn


def main():

    #parse parameters
    f,s = inputHandler()
    path = sys.argv[-1]

    #init pathfinder
    pf = PathFinder(path)
    files = pf.search(f,s)#grab files

    #output
    for doc in files:
        print(doc)
    
    #output execution time
    print("Execution Time ::  %s seconds " % round((time.time() - startTime),3))


if __name__ == "__main__":
    main()
