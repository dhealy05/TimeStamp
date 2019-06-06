import simulate_variants
import plot_moving_average

def index_translator(name):
    if name == 'normal':
        return 'index'
    elif name == 'normal_optimized':
        return 'readjusted_index'
    elif name == 'raw':
        return 'pred'
    elif name == 'raw_optimized':
        return 'readjusted_index_unadjusted'

def variant_translator(average, partition):
    if average == True:
        if partition == "full_set":
            return "readjusted_average"
        elif partition == "short_term":
            return "readjusted_average_index_8_offset"
        elif partition == "medium_term":
            return "readjusted_average_index_3"
        elif partition == "long_term":
            return "readjusted_average_index_7"
    else:
        if partition == "full_set":
            return "readjusted_median"
        elif partition == "short_term":
            return "readjusted_median_index_8_offset"
        elif partition == "medium_term":
            return "readjusted_median_index_3"
        elif partition == "long_term":
            return "readjusted_median_index_7"

#simulate_variants.simulate_all_variants()

#plot_moving_average.plot_ma(index_translator('normal'), variant_translator(True, 'full_set'), ma_frames = int(96*10), days_offset = 0)

plot_moving_average.animate_ma(index_translator('raw'), variant_translator(True, 'full_set'), ma_frames = int(96*10))
