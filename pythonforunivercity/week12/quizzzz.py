
class City:
  nbCity = 0
  def __init__(s,city,country,lat,long,temp):
    s.city = city; s.country = country; s.lat = lat
    s.long = long; s.temp = temp; City.nbCity += 1
class Country:
  nbCountry = 0
  def __init__(self,name,population,EU,coastline):
    self.con = name ; self.population = population
    self.EU = EU ; self.coastline = coastline

def readCity():
  myCity = []
  with open('Cities.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity

def test_readCity(myCity):
  for c in myCity:
    print(c.city,c.country,c.lat,c.long,c.temp)
def readCountry():
  myCountry = []
  with open('Countries.csv') as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      country,population,EU,coastline = cc[0], cc[1], cc[2], cc[3]
      myCountry.append(Country(country,population,EU,coastline))
  return myCountry

def q01(myCity, myCountry):
  countryeunotco = []
  for i in myCountry:
    if i.EU == 'yes' and i.coastline =='no':
      countryeunotco.append(i.con)
  averrangetem = {}
  for i in myCity:
    if i.country in countryeunotco:
      if i.country not in averrangetem.keys():
        averrangetem[i.country] = [i.temp]
      elif i.country in averrangetem.keys():
        averrangetem[i.country].append(i.temp)
  for k in averrangetem.keys():
    aver = sum(averrangetem[k])/len(averrangetem[k])
    averrangetem[k] = aver
  for k,v in averrangetem.items():
    print(f'{k}: {v:.2f}')
def q02(myCity, myCountry):
  con = []
  for i in myCountry:
    if i.EU == 'no' :
      con.append(i.con)
  max = 0
  min = 99999
  for i in myCity:
    if i.country in con:
      if max < i.temp:
        max = i.temp
        nmax = i.country
  for i in myCity:
    if i.country in con:
      if min > i.temp:
            min = i.temp
            nmin = i.country
  print(f'The highest average city temperature: {nmax} ({max:.2f})')
  print(f'The lowest average city temperature: {nmin} ({min:.2f})')
### main begins here
myCity = readCity()
myCountry = readCountry()
q01(myCity,myCountry)
q02(myCity,myCountry)