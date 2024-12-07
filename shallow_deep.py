#diff between sh_cpy and dp_cpy
import copy

original=[[1,2],[3,4]]
sh_copy=copy.copy(original)
dp_copy=copy.deepcopy(original)
print(original)
print(original)
original[0][0]=20
print(sh_copy)
print(dp_copy)