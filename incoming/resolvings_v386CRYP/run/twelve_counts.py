import sys
sys.path.insert(0, __import__('os').path.join(__import__('os').path.dirname(__file__), '..', '..', '..', 'kits/Natural_Networking_TWO_Improving_Kit/Natural_Networking_Test_Kit_v368'))
from resolver import _1_self_coupling
def surf(carry, offering):
    s, c = _1_self_coupling(carry, offering); return dict(s).get(0, 0)
print('empty carry, offerings at one sharing:')
for off in [[(0,1),(0,-1)], [(0,1),(0,1),(0,-1)], [(0,1),(0,1),(0,1),(0,-1),(0,-1)], [(0,-1),(0,-1),(0,1)]]:
    print('  ', [p for _,p in off], '-> surface', surf([], off))
print('carry (0,+1): the carry itself appends -1; offerings:')
for off in [[], [(0,1)], [(0,-1)], [(0,1),(0,1)], [(0,1),(0,1),(0,1)]]:
    print('  ', [p for _,p in off], '-> surface', surf([(0,1,1,0)], off))
