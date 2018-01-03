largest_histogram = lambda his: max(min(his[i:j])*(j-i) for i in range(len(his)) for j in range(i+1, len(his)+1))
