
W, H = 1000, 600
direction = [0, 1]
angle = [0, 1, 2]

#ball
green = (0,255,0)
rad = 15
b_x, b_y = W/2 - rad, H/2 - rad
b_vel_x, b_vel_y = 0.6, 0.6

#paddle
pink = (255, 0, 127)
pad_w, pad_h = 20, 120
left_pad_y = right_pad_y = H/2 - pad_h/2
left_pad_x, right_pad_x = 100 - pad_w/2, W - (100 - pad_w/2)
left_pad_vel = right_pad_vel = 0

#gadget
left_gadget = right_gadget = 0
left_gad_rem = right_gad_rem = 5