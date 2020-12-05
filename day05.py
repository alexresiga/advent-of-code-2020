print(max(seats := [int(t.strip().translate(str.maketrans('FBLR', '0101')), 2) for t in open('data.in').readlines()]))
next(print(seat + 1) for seat in seats if seat + 1 not in seats and seat + 2 in seats)
