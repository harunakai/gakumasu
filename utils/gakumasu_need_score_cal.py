import math

class gakumasu_need_score_cal:
    def __init__(self, end_rank_dict, required_score):
        self.end_rank_dict = end_rank_dict
        self.required_score = required_score
        

    def set_data(self, need_score, end_rank, vo, da, vi):
        self.end_rank = end_rank
        self.vo = vo + 30
        self.da = da + 30
        self.vi = vi + 30
        if self.vo > 1500:
            self.vo = 1500
        if self.da > 1500:
            self.da = 1500
        if self.vi > 1500:
            self.vi = 1500
        self.need_score = need_score

    def three_size(self):
        return math.floor((self.vo + self.da + self.vi)*2.3)
    
    def get_end_rank_score(self):
        if self.end_rank in self.end_rank_dict.keys():
            return self.end_rank_dict[self.end_rank]
        return 0
    
    def get_required_score(self):
        bottom, top = self.need_score, self.need_score+1
        #print(bottom, top)
        other_score = self.get_end_rank_score() + self.three_size()
        self.bottom = bottom - other_score
        self.top = top - other_score
        print(other_score, self.bottom,self.top)
        return self.get_bottom(), self.get_top()
    

    def get_bottom(self):
        bottom = 0
        if self.bottom < 0:
            return 0
        for start, end, func in self.required_score:
            if start <= self.bottom <= end:
                bottom = func(self.bottom)
                return bottom
        raise ValueError('bottom too big')

    def get_top(self):
        top = 0
        if self.top < 0:
            return 0
        for start, end, func in self.required_score:
            if start <= self.top <= end:
                top = func(self.top)
                return top
        raise ValueError('top too big')