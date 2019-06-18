import re
import itertools

class Utilities:
    
    def __init__(self, path = './corpus/digits-database.data'):
        self.path = path
        self.regex = re.compile('(0|1){2,}')
        self.regexno = re.compile('(\s)+[0-9]{1}')
        
    
    def generate_indices(self):
        _dict = []
        with open(self.path, 'r') as _f:
            pivote = 0
            flag = False
            lineno = 0
            for line in _f:
                if self.regex.match(line)!=None and not flag:
                    pivote = lineno
                    flag = True
                    
                if self.regexno.match(line)!=None and flag:
                    _dict.append((int(line.replace(' ','')),pivote,lineno))
                    flag = False
                lineno += 1
            _f.close()
        #print("DATOS:")
        #print(_dict)
        return _dict

    def get_digit(self,_slice, _end):
        data = []
        with open(self.path, 'r') as _f:
            for line in itertools.islice(_f, _slice, _end):
                data.append([int(i) for i in line.lstrip().rstrip()])
            
            _f.close()
        return data
