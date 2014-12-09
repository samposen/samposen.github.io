def File2Dict(filename):
   fid = open(filename)
   matches = [] # List for matches
   while 1:
      line = fid.readline()
      if not line:
         break
      field = line[:4]
      if field=='####':
         matches.append(match()) # Make new match
      else:
         value = line[5:]
         matches[-1].AddField(field, value) # Add data to last match
   return matches
      
class match:
   """Holds the data corresponding to a single game of foosball."""
   def __init__(self):
      """ Creates a dictionary to hold the fields of a foosball match."""
      self.data = {}
      
   def AddField(self, field, value):
      self.data[field] = value
      
   def GetValue(self, field):
      return self.data[field]
      
   def DispData(self):
      for field in self.data:
         print (field, self.data[field])
