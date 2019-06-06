import simulate_variants
import plot_moving_average

#simulate_variants.simulate_all_variants()

plot_moving_average.plot_ma("pred", variant = 'readjusted_average', ma_frames = int(96*10), days_offset = 0)

#plot_moving_average.animate_ma("pred", variant='readjusted_average', ma_frames = int(96*10))
