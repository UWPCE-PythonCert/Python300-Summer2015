class Take(object):

    def __init__(self,num,a_list):
        self.num = num
        self.current_indx = 0
        
        if not hasattr(a_list,'__getitem__'):
            raise TypeError('a_list needs to implement __getitem__')
        self.a_list = a_list

    def __iter__(self):
        return self

    def next(self):
        start_indx = self.current_indx
        end_indx = self.current_indx+self.num
        result = self.a_list[start_indx:end_indx]
        if len(result) == 0:
            raise StopIteration()
        self.current_indx += 1
        return result

if __name__ == '__main__':
    for slice in Take(3,range(4)):
        print slice