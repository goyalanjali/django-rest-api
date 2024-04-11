class hashmap:
    dict = {
    'val1' : 32,
    'val2' :54,
    'val3' : 45,
    'val4' : 98
    }

    def get_hashmap(self,key):
        s = 0
        for char in key:
            s += ord(char)

        return s % 4


hm = hashmap()
#hm.get_hashmap(hm.dict.get('val1')) 
#print(hm.get_hashmap('val2'))
print(hm.get_hashmap(dict('val1')))
#print(dict['val1'])  
#print(hm.dict.get('val1'))     





