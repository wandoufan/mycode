

filter_func = (lambda v: len(v.text) > 1 and v.aggregation > self.min_aggregation and 
                                v.freq > self.min_freq and v.left > self.min_entropy and v.right > self.min_entropy)