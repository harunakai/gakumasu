import math

class gakumasu_calculater:
    def __init__(self, rank_dict, end_rank_dict, end_score_rank):
        self.rank_dict = rank_dict
        self.end_rank_dict = end_rank_dict
        self.end_score_rank = end_score_rank


    def set_data(self, end_rank, end_score, vo, da, vi):
        self.end_rank = end_rank
        self.end_score = end_score
        self.vo = vo
        self.da = da
        self.vi = vi

    def get_end_rank_score(self):
        if self.end_rank in self.end_rank_dict.keys():
            return self.end_rank_dict[self.end_rank]
        return 0
    
    def three_size(self):
        return math.floor((self.vo + self.da + self.vi)*2.3)
    
    def get_end_score(self):
        for start, end, func in self.end_score_rank:
            if start <= self.end_score <= end:
                return math.floor(func(self.end_score))
        raise ValueError('end_score is out of range')

    def get_score(self):
        return self.get_end_rank_score() + self.three_size() + self.get_end_score()

    def get_rank(self):
        score = self.get_score()
        for start, end, rank in self.rank_dict:
            if start <= score <= end:
                return rank
        raise ValueError('score is out of range')

