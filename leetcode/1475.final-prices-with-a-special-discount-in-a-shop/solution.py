class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # elements: (price, index)
        price_stack = []
        output = [price for price in prices]
        for i in range(len(prices)):
            price = prices[i]
            while len(price_stack) > 0:
                peeked_price, peeked_index = price_stack[len(price_stack) - 1]
                if peeked_price < price:
                    break
                
                prev_price, index = price_stack.pop()
                output[index] = prev_price - price
                # print(output, "{}-{}".format(prev_price, index), "{}-{}".format(price, i))
            price_stack.append((price, i))


        return output