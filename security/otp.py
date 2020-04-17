ALPHABET_SIZE = 26

def add_padding(texts, pad):
  for i, t in enumerate(texts):
    for j, c in enumerate(t):
      mod_val = ord('a')
      if c.isupper():
        mod_val = ord('A')

      new_chr_ord = ord(c) + pad.get(j, 0)
      chr_difference = (new_chr_ord - mod_val) % ALPHABET_SIZE
      new_chr_ord = mod_val + chr_difference
      new_chr = chr(new_chr_ord)
      texts[i][j] = new_chr


def difference(c1, c2):
  dif = (ord(c2) - ord(c1)) % ALPHABET_SIZE
  return dif

def difference_string(s1, s2):
  to_return = []
  for i in range(len(s1)):
    to_return.append(difference(s1[i], s2[i]))
  return to_return


texts = [ 'LpaGbbfctNiPvwdbjnPuqolhhtygWhEuafjlirfPxxl',\
          'WdafvnbcDymxeeulWOtpoofnilwngLhblUfecvqAxs',\
          'UijMltDjeumxUnbiKstvdrVhcoDasUlrvDypegublg',\
          'LpaAlrhGmjikgjdmLlcsnnYmIsoPcglaGtKeQcemiu',\
          'LpaDohqcOzVbglebjPdTnoTzbyRbuwGftflTliPiqp']

texts = [list(t) for t in texts]  

pad = {
  0 : 8,
  1 : 18,
  2 : 4,
  3 : 12,
  4 : 3,
  5 : 1,
  6 : 12,
  7 : 2,
  8 : 0,
  9 : 6,
  10: 6,
  11: 7,
  12:13,
  13:17,
  14:10,
  15:7,
  16:4,
  17:19,
  18:15,
  19:0,
  20:1,
  21:0,
  22:10,
  23:1,
  24:11,
  25:15,
  26:16,
  27:7,
  28:12,
  29:11,
  30:0,
  31:3,
  32:2,
  33:25,
  34:2,
  35:0,
  36:22,
  37:22,
  38:14,
  39:18,
  40:3,
  41:11,
  42:6
}

add_padding(texts, pad)

texts = [''.join(t) for t in texts]

print(difference_string('l', 'r'))

padding = [pad[key] for key in sorted(pad)]
print(padding)
print(texts)