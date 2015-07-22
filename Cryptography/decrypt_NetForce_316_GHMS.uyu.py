#!/usr/bin/python

encrypted_text = "Bg`kkdmfd.mnsdr9Sgd.ehkd.&mdsenqbd-dmb&b`madcdbqxosdcvhsg`oqhu`sdjdx-Dudqx53ahsrbgtmjv`rdmbqxosdc`s`shldtrhmfsgdq`v`kfnqhsgl+sgdr`ldb`madcnmdsncdbqxos-axQhudrs+Rg`lhq+%@ckdl`m"

decrypted_text = "Deciphered text: "

print "Decrypting now..."

for c in encrypted_text:
	num = ord(c)
	new_num = num+1
	new_char = chr(new_num)
	decrypted_text = decrypted_text + new_char

print decrypted_text