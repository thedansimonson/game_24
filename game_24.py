from itertools import permutations 


###############
# Calculation #
###############

ops = {"+": lambda x,y: x+y,
       "-": lambda x,y: x-y,
       "*": lambda x,y: x*y,
       "/": lambda x,y: float(x)/float(y)}

def permute_ops(*args):
    #if we have a single digit, quit
    if len(args) == 1: return [(args[0],args[0])]
    
    perms = []
    for partition in range(1,len(args)):
        
        # split the digits into pieces first, compute the pieces
        left_args,  right_args  = args[:partition],args[partition:]
        left_perms, right_perms = permute_ops(*left_args),permute_ops(*right_args)
        
        # for each permutation in the pieces, compute the values and construct the 
        # symbolic representation
        for left_sym, left_value in left_perms:
            for right_sym, right_value in right_perms:
                for op in ops:
                    try:
                        perms.append(((op,left_sym,right_sym), 
                                      ops[op](left_value, right_value)))
                    except ZeroDivisionError:
                        pass

    return perms


def find_target(target,digits):
    dig_perms = permutations(digits)
    return [(sym,v) for dig_seq in dig_perms 
                    for sym,v in permute_ops(*dig_seq) if v == target]

############
# ANALYSIS #
############

def pair_matrix():
    pairs = [[i,j] for i in range(1,11) for j in range(1,11)]
     
    rows = []
    for pair in pairs:
        print "Running:",pair
        cols = [len(find_target(24,pair+quair)) for quair in pairs]
        rows.append(cols)

    return rows


if __name__ == "__main__":
    matrix = pair_matrix()
    print "\n".join(["\t".join([str(c) for c in cols]) for cols in matrix])
            
