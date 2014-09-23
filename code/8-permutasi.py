 def Permutasi(string, storage, prefix=""):
   if len(string) == 1:
      storage.append(prefix + string)
   else:
      for i in range(len(string)):
         Permutasi(string[:i]+string[i+1:], storage, prefix+string[i])
