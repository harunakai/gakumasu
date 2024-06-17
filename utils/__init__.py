from .gakumasu_calculater import gakumasu_calculater
from .gakumasu_remain_cal import gakumasu_remain_cal
from .gakumasu_need_score_cal import gakumasu_need_score_cal


rank_dict = {
    (4500,  5999,  'C+'),
    (6000,  7999,  'B' ),
    (8000,  9999,  'B+'),
    (10000, 11499, 'A' ),
    (11500, 12999, 'A+'),
    (13000, 13999, 'S' ),
}
end_rank_dict = {
    '1': 1700,
    '2':  900,
    '3':  500,
}

end_score_rank = [
    (0, 5000, lambda x: 0.3  *x),
    (5001, 10000, lambda x: 0.15 * x + 750),
    (10001, 20000, lambda x: 0.08 * x + 1450),
    (20001, 30000, lambda x: 0.04 * x + 2250),
    (30001, 40000, lambda x: 0.02 * x + 2850),
    (40001, 50000, lambda x: 0.01 * x + 3250),
]

required_score = [
    (0, 1500, lambda x: x / 0.3),
    (1501, 2250, lambda x: (x - 750) / 0.15),
    (2251, 3050, lambda x: (x - 1450) / 0.08),
    (3051, 3450, lambda x: (x - 2250) / 0.04),
    (3451, 3650, lambda x: (x - 2850) / 0.02),
    (3651, 3750, lambda x: (x - 3250) / 0.01)
]

romaji2hanzi = {
    'saki': '咲季',
    'temari': '手鞠',
    'kotone': '琴音',
    'china': '千奈',
    'hiro': '广',
    'kunio': '邦夫',
    'mao': '真央',
    'misuzu': '美铃',
    'rinami': '莉波',
    'ririya': '莉莉娅',
    'sena': '星南',
    'sumika': '清夏',
    'ume': '佑芽',
    'asari': '亚纱里'
}

def get_rank_cal():
    return gakumasu_calculater(rank_dict, end_rank_dict, end_score_rank)

def get_remain_cal():
    return gakumasu_remain_cal(rank_dict, end_rank_dict, required_score)

def get_need_score_cal():
    return gakumasu_need_score_cal(end_rank_dict, required_score)

