import os
import commands

# os.system("g++ main.cpp")
# os.system('g++ -o main main.cpp')
# os.system('xxd -c10 -b ./main')
# os.system('./main')

os.system("g++ main_encrypt.cpp encryption.cpp decryption.cpp keylib.cpp" )
os.system('g++ -o ./encrypt main_encrypt.cpp encryption.cpp decryption.cpp keylib.cpp')

os.system("g++ main_decrypt.cpp encryption.cpp decryption.cpp keylib.cpp" )
os.system('g++ -o ./decrypt main_decrypt.cpp encryption.cpp decryption.cpp keylib.cpp')
# os.system('xxd -c10 -b main')
# os.system('main')
comp_output = "<strong>C++ compilation output:<strong><br>"+ commands.getstatusoutput('./encrypt')[1].replace('\n', '<br>')
comp_output += "<br>---<br>"+ commands.getstatusoutput('./decrypt')[1].replace('\n', '<br>')

print "****", comp_output.replace('<strong>', "").replace('<br>', '\n')