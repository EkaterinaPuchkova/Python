seq = ''
sheet = ''
for chart in range(32, 128):
    seq += '{} - {}\t'.format(chart, chr(chart))
    if not (chart - 31) % 10:
        sheet += '{}\n'.format(seq)
        seq = ''
sheet += '{}\n'.format(seq)
print(sheet)