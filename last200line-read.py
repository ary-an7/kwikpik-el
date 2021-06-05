def Last200lines(file):
    with open(file) as f:
        for line in (f.readlines() [-200:]):
            print(line, end ='')
  
  
if __name__ == '__main__':
    file = 'cron.log'
    try:
        Last200lines(file)
    except:
        print('File not found')