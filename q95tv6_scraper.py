#!/usr/bin/env python3.8
import time
from datetime import datetime
from math import inf
from q95tv6 import get_prices, alert_popup, urls


if __name__ == '__main__':
    cheapest_store = 'Appliances Online'
    cheapest_price = inf
    update = False
    prices = {'Appliances Online':inf, 'JB-HiFi':inf, 'Appliance Central':inf, 'Videopro':inf, 'Bing Lee':inf, 'Harvey Norman':inf, 'The Good Guys':inf}

    while True:
        new_prices = get_prices()

        for i in prices:
            if prices[i] != new_prices[i]:
                prices = new_prices
                update = True
                break

        if update:
            new_cheapest_store = next(iter(new_prices))

            current_time = datetime.now().strftime('%I:%M:%S%p')
            f = open('log.txt', 'a')
            print('--------------------Update at ' + str(current_time) + '------------------')
            f.write('--------------------Update at ' + str(current_time) + '------------------'+'\n')
            for i in new_prices:
                if new_prices[i]:
                    if i in ['Appliances Online', 'Appliance Central']:
                        if new_prices[i] < inf:
                            print(i + ':\t' + '$'+str(new_prices[i])[0:1]+','+str(new_prices[i])[1:])
                            f.write(i + ':\t' + '$'+str(new_prices[i])[0:1]+','+str(new_prices[i])[1:]+'\n')
                        else:
                            print(i + ':\t' + 'N/A')
                            f.write(i + ':\t' + 'N/A\n')

                    else:
                        if new_prices[i] < inf:
                            print(i + ':\t\t' + '$'+str(new_prices[i])[0:1]+','+str(new_prices[i])[1:])
                            f.write(i + ':\t\t' + '$'+str(new_prices[i])[0:1]+','+str(new_prices[i])[1:]+'\n')
                        else:
                            print(i + ':\t\t' + 'N/A')
                            f.write(i + ':\t\t' + 'N/A\n')

                else:
                    print('Error')
                    f.write('Error'+'\n')
            print('----------------------------------------------------------')
            f.write('----------------------------------------------------------'+'\n\n')
            f.close()

            if new_prices[new_cheapest_store] < cheapest_price:
                new_cheapest_price = new_prices[new_cheapest_store]
                cheapest_store = new_cheapest_store
                cheapest_price = new_cheapest_price
                new_cheapest_price = '$'+str(new_cheapest_price)[0:1]+','+str(new_cheapest_price)[1:]
                alert_popup('Price Alert!', 'New low price at ' + new_cheapest_store + '  ' + new_cheapest_price, urls[cheapest_store])

        else:
            current_time = datetime.now().strftime('%I:%M:%S%p')
            f = open('log.txt', 'a')
            print('--------------------No Updates ' + str(current_time) + '-----------------'+'\n')
            f.write('--------------------No Updates ' + str(current_time) + '-----------------'+'\n')
            f.close()

        update = False
        break ## Remove if you want to run the script every 15 minutes (or add a batch file to the scheduler).
        time.sleep(900)
