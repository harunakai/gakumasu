import math

class gakumasu_remain_cal:
    def __init__(self, rank_dict, end_rank_dict, required_score) -> None:
        self.rank_dict = rank_dict
        self.end_rank_dict = end_rank_dict
        self.required_score = required_score
        self.bottom = 0
        self.top = 0

    def set_data(self, wanted_rank, end_rank, vo, da, vi):
        self.wanted_rank = wanted_rank
        self.end_rank = end_rank
        self.vo = vo
        self.da = da
        self.vi = vi


    def three_size(self):
        if self.end_rank == '1':
            return math.floor((self.vo + self.da + self.vi + 90)*2.3)
        else:
            return math.floor((self.vo + self.da + self.vi)*2.3)
    

    def get_end_rank_score(self):
        if self.end_rank in self.end_rank_dict.keys():
            return self.end_rank_dict[self.end_rank]
        return 0
    
    def get_required_score(self):
        bottom, top = 0,0
        for start, end, rank in self.rank_dict:
            if rank == self.wanted_rank:
                bottom, top = start, end
                break
        #print(bottom, top)
        other_score = self.get_end_rank_score() + self.three_size()
        self.bottom = bottom - other_score
        self.top = top - other_score
        #print(other_score, self.bottom,self.top)
        return self.get_bottom(), self.get_top()
    def get_bottom(self):
        bottom = 0
        if self.bottom < 0:
            return 0
        for start, end, func in self.required_score:
            if start <= self.bottom <= end:
                bottom = math.ceil(func(self.bottom))
                return bottom
        raise ValueError('bottom too big')

    def get_top(self):
        top = 0
        if self.top < 0:
            return 0
        for start, end, func in self.required_score:
            if start <= self.top <= end:
                top = math.floor(func(self.top))
                return top
        raise ValueError('top too big')

                
