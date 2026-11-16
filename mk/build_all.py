import sys, json
sys.path.insert(0, '.')
import common
import a_game, b_evidence, c_rest, d_review, e_gamaan, f_csr, h_layers, i_kuran, j_poll, k_sparks
bad = common.finish()
json.dump([f'simorgh:{s}' for s in ['game','evidence','history','strategy','action','project']], open(f'{common.R}/data/simorgh/order.json','w'), ensure_ascii=False)
print('entries', len(common.CREATED)); print('dropped links', bad)
import collections
print(collections.Counter(d['kind'] for d in common.CREATED.values()))
