
def main():

  homeInput = input('1. See Top 20 coins\n' 
                    '2. My Coins\n')
  
  while(True):


    if(homeInput == "1"):
      top20Input = input('\n1. Search for Coin\n'
                           '2. Sort by name\n'
                           '3. Sort by daily change\n'
                           '4. Go back\n')

      if(top20Input == "1"):
        saveCoinInput = input()
        break

      if(top20Input == "2"):
        break

      if(top20Input == "3"):
        break

      if(top20Input == "4"):
        break
    
    if(homeInput == "q"):
      break


if __name__ == '__main__':
  main()